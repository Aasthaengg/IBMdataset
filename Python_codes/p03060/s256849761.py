N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [v-c for v, c in zip(V, C)]
P_plus = [p if p > 0 else 0 for p in P]
print(sum(P_plus))