N=int(input())
p=[0]
q=[0]
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
for i in range(N):
  p.append(p[i]+A1[i])
  q.append(q[i]+A2[N-i-1])
ans=0
for j in range(N):
  ans=max(ans,p[j+1]+q[N-j])
print(ans)