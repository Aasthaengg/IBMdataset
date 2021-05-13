N,M = map(int, input().split())
scorebook = [[] for _ in range(N)]
for i in range(M):
    p,S = input().split()
    p = int(p)-1
    scorebook[p].append(S)
maru = 0
batu = 0
for score in scorebook:
    try:
        batu += score.index("AC")
        maru += 1
    except:
        pass
print(maru, batu)