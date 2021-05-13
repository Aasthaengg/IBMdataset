n = int(input())
a = list(map(int, input().split()))
tmp = 1
res = 0
for i in range(1,n):
  if a[i-1] == a[i]:
    tmp += 1
  else:
    res += tmp//2
    tmp = 1
res += tmp//2
print(res)