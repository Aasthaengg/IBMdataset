n,k = map(int,input().split())
h = [int(input()) for i in range(n)]
h = sorted(h)
ans = 10**9
for i in range(n-k+1):
  num = (h[i+(k-1)]-h[i])
  if num <= ans:
    ans = num
print(ans)