N,M = (int(T) for T in input().split())
Stud = [[] for TN in range(0,N)]
Check = [[] for TM in range(0,M)]
for TN in range(0,N):
    Stud[TN] = [int(T) for T in input().split()]
for TM in range(0,M):
    Check[TM] = [int(T) for T in input().split()]

GoPoint = [0]*N
for TN in range(0,N):
    MIND = 10**9
    for TM in range(0,M):
        Dist = abs(Stud[TN][0]-Check[TM][0])+abs(Stud[TN][1]-Check[TM][1])
        if Dist<MIND:
            MIND = Dist
            MINI = TM
    GoPoint[TN] = MINI+1
print('\n'.join(str(T) for T in GoPoint))