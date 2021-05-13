N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
cnt=0
for a,b in A:
  cnt+=(b-a+1)
print(cnt)