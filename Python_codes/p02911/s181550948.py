N, K, Q = map(int, input().split())
count = [0] * N
for _ in range(Q):
  count[int(input())-1] += 1
for c in count:
  if K - (Q - c) > 0:
    print('Yes')
  else:
    print('No')