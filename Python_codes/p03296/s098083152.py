n = int(input())
d = list(map(int,input().split()))
ans = 0
tmp = 0
for i in range(n-1):
  if d[i] == d[i+1] and tmp%2 ==0:
    tmp += 1
    ans += 1
  else:
    tmp = 0
print(ans)