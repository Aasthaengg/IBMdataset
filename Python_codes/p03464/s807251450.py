k = int(input())
A = list(map(int, input().split()))
m = M = 2
for a in A[::-1]:
  m += (-m)%a
  M += -(M%a) + a - 1
  if m > M:
    print(-1)
    break
else:
  print(m, M)