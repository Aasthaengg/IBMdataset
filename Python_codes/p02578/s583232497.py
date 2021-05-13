n = input()
a = list(map(int, input().split()))
maxi = 0
ans = 0
for i in range(len(a)):
  maxi = max(a[i],maxi)
  ans += maxi - a[i]
print(ans)