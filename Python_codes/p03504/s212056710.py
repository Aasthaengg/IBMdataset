import sys
input = sys.stdin.buffer.readline
from operator import itemgetter

def main():
    N,C = map(int,input().split())
    ch = [[] for _ in range(C)]
    l = 0
    for _ in range(N):
        s,t,c = map(int,input().split())
        l = max(l,t)
        ch[c-1].append((s,t))
    
    for x in ch:
        x.sort(key=itemgetter(0))

    imos = [0 for _ in range(l+2)]
    for x in ch:
        now = -1
        for st,ft in x:
            if st == now:
                imos[st] += 1
            else:
                imos[st-1] += 1
            imos[ft] -= 1
            now = ft
                
    for i in range(l+1):
        imos[i+1] += imos[i]
    
    print(max(imos))
    
if __name__ == "__main__":
    main()
