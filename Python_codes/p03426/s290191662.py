import sys
import itertools

input = sys.stdin.readline

def myindex(l, element, default=-1):
    if element in set(l):
        return l.index(element)
    else:
        return default

def main():
    H, W, D = map(int, input().split())
    grid = []; locale = [0]*(H*W)
    for i in range(H):
        tmp = list(map(int, input().split()))
        for j, t in enumerate(tmp):
            x, y = i+1, j+1
            locale[t-1] = (x, y)
        grid.append(tmp)
    
    power = []
    for k in range(H*W-D):
        fr = locale[k]
        to = locale[k+D]
        need = abs(fr[0]- to[0]) + abs(fr[1] - to[1])
        power.append(need)
    
    cum = []
    for d in range(D):
        cum.append([0] + list(itertools.accumulate(power[d::D])))

    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        d = (L-1)%D
        dnum = (L-1)//D
        drange = (R-L)//D
        ans = cum[d][dnum+drange] - cum[d][dnum]
        print(ans)
    
if __name__ == "__main__":
    main()
