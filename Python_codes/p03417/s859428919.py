N,M = (int(X) for X in input().split())
if N==1 or M==1:
    if N==M:
        print(1)
    else:
        print(max(N,M)-2)
else:
    Four = 4
    Six  = 2*(N+M-4)
    Nine = N*M-(Four+Six)
    print(Nine)