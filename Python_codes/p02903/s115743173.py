H, W, A, B = map(int, input().split())

ans = [['1' if (h<B and w<A) or (B<=h and A<=w) else '0' for w in range(W)] for h in range(H)]

for a in ans:
  print(''.join(a))