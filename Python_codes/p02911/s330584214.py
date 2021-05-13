from collections import Counter
N, K, Q = map(int, input().split())
A = Counter([int(input()) for _ in range(Q)])
[print("Yes" if K > Q - A.get(i+1, 0) else "No") for i in range(N)]
