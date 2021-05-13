X, Y, A, B, C = map(int, input().split())
Ap = list(map(lambda x: (int(x), 0), input().split()))
Bq = list(map(lambda x: (int(x), 1), input().split()))
Cr = list(map(lambda x: (int(x), 2), input().split()))

INF = 2 * 10**5 + 1

L = Ap + Bq + Cr
L.sort(reverse = True)

cnt = [0, 0, 0]
cntM = [X, Y, INF]
s = 0

ans = 0

for x, i in L:
  if s == X + Y:
    break
  elif cnt[i] < cntM[i]:
    ans += x
    cnt[i] += 1
    s += 1
  else:
    pass

print(ans)