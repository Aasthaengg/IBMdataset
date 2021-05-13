def turn():
  global drc
  if moves[drc][-1] != 0:
    moves[drc].append(0)
  drc=(drc+1)%2

def forward():
  moves[drc][-1]+=1
  
OP={"T":turn,"F":forward}

ops=input()
target=list(map(int,input().split()))
moves=[[0],[0]]
drc=0
first_F=0

# データ加工
for i,o in enumerate(ops):
  if o=="T" or i+1==len(ops):
    first_F=i
    break

for i in range(first_F,len(ops)):
  OP[ops[i]]()

# 組み合わせ演算
x_set=set([first_F])
for move in moves[0]:
  tmp_set=set()
  for xx in x_set:
    tmp_set.add(xx+move)
    tmp_set.add(xx-move)
  x_set=tmp_set
  
y_set=set([0])
for move in moves[1]:
  tmp_set=set()
  for yy in y_set:
    tmp_set.add(yy+move)
    tmp_set.add(yy-move)
  y_set=tmp_set

if target[0] in x_set and target[1] in y_set:
  print("Yes")
else:
  print("No")
