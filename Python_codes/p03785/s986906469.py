n,c,k=map(int,input().split())
t=[]
for i in range(n):
  T=int(input())
  t.append(T)

t.sort()
ans=1
pas=0
depa=t[0]+k

for i in range(n):
  if c==pas or depa<t[i]:
    ans+=1
    pas=1
    depa=t[i]+k
  else:
    pas+=1
print(ans)
