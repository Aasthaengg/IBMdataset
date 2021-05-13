k = int(input())
a, b = [int(i) for i in input().split()]
ans = 'NG'
for i in range(a, b+1):
  if i % k == 0:
    ans = 'OK'
print(ans)