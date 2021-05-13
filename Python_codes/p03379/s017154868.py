import bisect

N = int(input())
Xs = list(map(int, input().split()))

Ss = sorted(Xs)

for i in range(N):
  j = bisect.bisect_left(Ss, Xs[i])
  if j < N//2:
    print(Ss[N//2])
  else:
    print(Ss[N//2-1])