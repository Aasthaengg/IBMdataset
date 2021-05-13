N, Q = map(int, input().split())
S = list(input())
L = [0]
cnt = 0

for i in range(1, N):
  if S[i-1] == "A" and S[i] == "C":
    cnt += 1
  L.append(cnt)

for _ in range(Q):
  l, r = map(int, input().split())
  print(L[r-1] - L[l-1])