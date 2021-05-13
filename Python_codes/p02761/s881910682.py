N, M = map(int, input().split())
s_c = [list(map(int, input().split())) for _ in range(M)]

if N == 1:
  a, b = 0, 10**N
elif N >= 2:
  a, b = 10**(N-1), 10**N

ans = '-1'
for i in range(a, b):
  flag = True
  for j in range(M):
    if str(i)[s_c[j][0]-1] != str(s_c[j][1]):
      flag = False
  if flag:
    ans = i
    break

print(ans)