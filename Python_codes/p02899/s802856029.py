n = int(input())
a = list(map(int,input().split()))
ans = [0 for i in range(n)]
for i,vol in enumerate(a):
  ans[vol-1]=i+1
print(*ans)