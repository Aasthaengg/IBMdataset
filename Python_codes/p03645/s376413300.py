N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]
L_1 = set([l[1] for l in L if l[0]==1])
L_2 = set([l[0] for l in L if l[1]==N])
print("POSSIBLE" if L_1&L_2 else "IMPOSSIBLE")