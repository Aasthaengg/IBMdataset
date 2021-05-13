from heapq import heappush,heappop

S = input()
slist = "abcdefghijklmnopqrstuvwxyz"

if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

lis =[]
T = S
if len(S)<26:
    Sset = set(S)
    for s in slist:
        if s not in Sset:
            print(S+s)
            exit()
else:
    while len(S)>0:
        lis.append(S[-1])
        lis.sort()
        S = S[:-1]
        for s in lis:
            if S + s > T:
                print(S + s)
                exit()
