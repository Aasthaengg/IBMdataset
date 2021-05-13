n, m, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m-1):
  if x > a[-1] or x < a[0]:
    ans1 = 0
    ans2 = 0
  elif a[i] < x <a[i+1]:
    ans1 = len(a[:i+1])
    ans2 = len(a[i+1:])
print(min(ans1, ans2))