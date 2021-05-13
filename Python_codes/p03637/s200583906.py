import sys
N=int(input())
alist=list(map(int,input().split()))

s1=[]
s2=[]
s4=[]

for a in alist:
  if a%2==1:
    s1.append(a)
  elif a%4==0:
    s4.append(a)
  else:
    s2.append(a)
#print(s1,s2,s4)

answer_list=[]
last=4
for i in range(N):
  if last==4:
    if s1:
      answer_list.append(s1.pop())
      last=1
    elif s2:
      answer_list.append(s2.pop())
      last=2
    else:
      answer_list.append(s4.pop())
      last=4
  elif last==2:
    if s2:
      answer_list.append(s2.pop())
      last=2
    elif s4:
      answer_list.append(s4.pop())
      last=4
    else:
      print("No")
      sys.exit(0)
  elif last==1:
    if s4:
      answer_list.append(s4.pop())
      last=4
    else:
      print("No")
      sys.exit(0)
      
#print(answer_list)
print("Yes")