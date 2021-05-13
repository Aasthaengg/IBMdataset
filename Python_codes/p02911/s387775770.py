N,K,Q = map(int,input().split())

scores = [K] * N

for i in range(Q):
  a = int(input())
  scores[a - 1] += 1

for s in scores:
  print(("No","Yes")[s - Q > 0])
