N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

cards = []
for _ in range(M):
  b,c = map(int,input().split())
  cards.append([c,b])
cards.sort(key=lambda x: -x[0])

res = 0
idx = 0
left = cards[idx][1]
for i,a in enumerate(A):
  if a > cards[idx][0]:
    res += sum(A[i:])
    break
  else:
    res += cards[idx][0]

    left -= 1
    if left <= 0:
      idx += 1
      if idx >= M:
        if i+1 < N:
          res += sum(A[i+1:])
        break
      else:
        left = cards[idx][1]

print(res)