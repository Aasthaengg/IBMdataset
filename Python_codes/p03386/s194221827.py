A, B, K = map(int, input().split())
L_1 = set([i for i in range(A, min(A+K, B+1))])
L_2 = set([i for i in range(max(A, B-K+1), B+1)])
L = sorted(L_1|L_2)
for l in L:
  print(l)