n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]

ans = float("inf")
for i in range(4**n):
  T = [0]*4
  C = [0]*4
  for j, l in enumerate(L):
    T[(i>>(2*j))&3] += l
    C[(i>>(2*j))&3] += 1
  ta, tb, tc = T[1:]
  if ta == 0 or tb == 0 or tc == 0:
    continue
  temp = 0
  temp += max(C[1]-1, 0)
  temp += max(C[2]-1, 0)
  temp += max(C[3]-1, 0)
  temp *= 10
  temp += abs(a-ta) + abs(b-tb) + abs(c-tc)
  ans = min(ans, temp)
print(ans)