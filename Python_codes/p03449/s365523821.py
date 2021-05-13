N=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))

MAX=0
for i in range(N):
  tmp = sum(a1[:i+1])+sum(a2[i:])
  MAX = max(MAX,tmp)

print(MAX)