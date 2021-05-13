n,c=map(int,input().split())
A=[]
for i in range(n):
  s,t,c=map(int,input().split())
  A.append((s,t,c))
A.sort(key=lambda x:(x[2],x[0],x[1]))
B=[]
s,t,c=A[0]

for i in range(1,n):
  s2,t2,c2=A[i]
  if c==c2 and t==s2:
    t=t2
  else:
    B.append((s-1,t,c))
    s,t,c=s2,t2,c2
B.append((s-1,t,c))

T=[0]*(10**5+1)
for s,t,c, in B:
  T[s]+=1
  T[t]-=1
for i in range(10**5):
  T[i+1]+=T[i]
print(max(T))

