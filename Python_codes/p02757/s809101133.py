n, p = map(int, input().split())
s = input()[::-1]
if p == 2:
  ans = 0
  for num, i in enumerate(s):
    if int(i)%2 == 0:
      ans += n-num
elif p == 5:
  ans = 0
  for num, i in enumerate(s):
    if int(i)%5 == 0:
      ans += n-num
else:
  C = [0]*p
  now = 0
  for num, i in enumerate(s):
    a = int(i)
    now = (now+pow(10, num, p)*a)%p
    C[now] += 1
  ans = C[0]
  for c in C:
    ans += c*(c-1)//2
print(ans)