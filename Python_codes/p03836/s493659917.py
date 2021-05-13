sx,sy,tx,ty=map(int,input().split())
ts_x=tx-sx
ts_y=ty-sy

answer_list=[]
#s->t
for i in range(ts_y):
  answer_list.append("U")
for i in range(ts_x):
  answer_list.append("R")
  
#t->s
for i in range(ts_y):
  answer_list.append("D")
for i in range(ts_x):
  answer_list.append("L")
  
#s->t
answer_list.append("L")
for i in range(ts_y+1):
  answer_list.append("U")
for i in range(ts_x+1):
  answer_list.append("R")
answer_list.append("D")

#t->s
answer_list.append("R")
for i in range(ts_y+1):
  answer_list.append("D")
for i in range(ts_x+1):
  answer_list.append("L")
answer_list.append("U")

print("".join(answer_list))