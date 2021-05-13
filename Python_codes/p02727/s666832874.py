X,Y,A,B,C = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)

AD = P[:X] + Q[:Y] + R
AD.sort(reverse=True)
print(sum(AD[:(X+Y)]))
exit(0)

### zanshi
ans = sum(P[:X]) + sum(Q[:Y])

pi, qi, ri = X-1, Y-1, 0
for _ in range(C+10):
  if P[pi] < R[ri] and P[pi] <= Q[qi]:
    ans += R[ri] - P[pi]
    pi, ri = pi-1, ri+1
  elif Q[qi] < R[ri] and P[pi] >= Q[qi]:
    ans += R[ri] - Q[qi]
    qi, ri = qi-1, ri+1
  if pi < 0 or qi < 0 or ri >= C:
    break
print(ans)