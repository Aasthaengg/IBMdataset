T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

a, b, ans = 0, 0, 0
n1 = (A1-B1)*T1
n2 = n1 + (A2-B2)*T2
if n2 == 0:
  print('infinity')
elif n1*n2 < 0:
  ans += 2 * (abs(n1)//abs(n2))
  if abs(n1)%abs(n2) > 0:
    ans += 1
  print(ans)
else:
  print(0)