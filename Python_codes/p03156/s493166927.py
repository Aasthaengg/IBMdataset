N=int(input())
AB=input().split()
AB=[int(n) for n in AB]
P=input().split()
P=[int(n) for n in P]
q=[0,0,0]

for p in P:
  if (p<=AB[0]):
    q[0]+=1
  elif (AB[0]+1)<=p<=(AB[1]):
    q[1]+=1
  elif (AB[1]+1)<=p:
    q[2]+=1

print ('{}'.format(min(q)))
