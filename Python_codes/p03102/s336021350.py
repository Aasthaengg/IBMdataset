N, M, C = map(int, input().split())
B = list(map(int, input().split()))
As = [list(map(int, input().split())) for _ in range(N)]
print(sum(sum(a*b for a, b in zip(A, B))>-C for A in As))