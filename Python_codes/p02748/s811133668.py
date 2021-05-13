import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,m=map(int, input().split())
    la=list(map(int,input().split()))
    lb=list(map(int,input().split()))
    lm=[list(map(int,input().split())) for i in range(m)]
    nowari=min(la)+min(lb)
    warians=10**10
    for i in range(m):
        wari=la[(lm[i][0])-1]+lb[(lm[i][1])-1]-lm[i][2]
        if wari<warians:
            warians=wari
    print(min(nowari,warians))
resolve()