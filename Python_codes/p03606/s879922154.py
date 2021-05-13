N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
L2 = [l[1] - (l[0] -1) for l in L]
print(sum(L2))