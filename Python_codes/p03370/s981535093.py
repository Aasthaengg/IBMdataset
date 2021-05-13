N,X=list(map(int, input().split()))
m=[]
for i in range(N):
  m.append(int(input()))
X-=sum(m)
m.sort()
print(N+X//m[0])