n = input()
t, a = map(int, input().split())
h = list(map(int, input().split()))
ans = 1
min_err = 10 ** 9
for i, hn in enumerate(h):
  err = abs(a - (t - hn * 0.006))
  if err < min_err:
    min_err = err
    ans = i + 1
print(ans)