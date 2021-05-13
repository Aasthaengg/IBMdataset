N=int(input())
l=list(map(int,input().split()))
p=[0]*N
for i in range(N):
  if i<(N+1)//2:
    p[i]=l[N-1-2*i]
  else:
    p[i]=l[N-2*(N-i)]
print(*p)