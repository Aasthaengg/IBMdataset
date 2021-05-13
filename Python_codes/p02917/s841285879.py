n=int(input())
B=list(map(int,input().split()))
ans = 0

ans += B[0]
for i in range(n-2):
  ans += min(B[i],B[i+1])
ans += B[n-2]

print(ans)