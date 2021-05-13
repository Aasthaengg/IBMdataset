import bisect

N,M = map(int,input().split())
PY = [list(map(int,input().split())) for _ in range(M)]
L = [[] for _ in range(N)]

for P,Y in PY:
    bisect.insort_left(L[P-1],Y)

for P,Y in PY:
    P_ans = str(P).zfill(6)
    Y_ans = str(bisect.bisect_right(L[P-1],Y)).zfill(6)
    print(P_ans,Y_ans,sep="")