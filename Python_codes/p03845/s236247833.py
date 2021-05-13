n = int(input())
T = list(map(int, input().split()))
m = int(input())
P = [list(map(int, input().split())) for _ in range(m)]
for p in P:
    tmp_l = T.copy()
    tmp_l[p[0]-1] = p[1]
    print(sum(tmp_l))