N = int(input())
T = list(map(int, input().split()))
M = int(input())
D = [list(map(int, input().split())) for _ in range(M)]

for m in range(M):
    tmp_T = T[:]
    tmp_T[D[m][0]-1] = D[m][1]
    print(sum(tmp_T))