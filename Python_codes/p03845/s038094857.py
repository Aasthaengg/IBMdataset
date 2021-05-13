N = int(input())
T_s = list(map(int,input().split()))
M = int(input())
PX_s = [list(map(int,input().split())) for _ in range(M)]
SUM = sum(T_s)
for P,X in PX_s:
    print(SUM - (T_s[P-1] - X))