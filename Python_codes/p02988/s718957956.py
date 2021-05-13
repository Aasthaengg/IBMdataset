n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(n-2):
  ls = p[i:i+3]
  if ls[0] < ls[1] < ls[2] or ls[0] > ls[1] > ls[2]:
    ans += 1
print(ans)