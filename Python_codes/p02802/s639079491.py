N,M = map(int,input().split())
A = [0]*(N+1)
ac = 0
pe = 0
for i in range(M):
    p,S = input().split()
    if A[int(p)] == -1:
        continue
    if S == "AC":
        ac += 1
        pe += A[int(p)]
        A[int(p)] = -1
    else:
        A[int(p)] += 1
print(ac,pe)