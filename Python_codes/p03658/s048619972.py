from itertools import combinations

N, K = map(int, input().split())
L = sorted(list(map(int, input().split())), reverse=True)
ans = sum(L[:K])
print(ans)
