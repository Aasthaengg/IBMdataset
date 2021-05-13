from itertools import accumulate, product
def solve():
    N,W = map(int,input().split())
    value = [list() for _ in range(4)]
    w1 = None
    for i in range(N):
        w,v = map(int,input().split())
        if i == 0:
            w1 = w
        value[w-w1].append(v)
    
    acc = []
    for i in range(4):
        value[i].sort(reverse=True)
        acc.append(list(accumulate(value[i])))
    
    comb = []
    for i_0 in range(len(acc[0]) + 1):
        for i_1 in range(len(acc[1]) + 1):
            for i_2 in range(len(acc[2]) + 1):
                for i_3 in range(len(acc[3]) + 1):
                    comb.append((i_0,i_1,i_2,i_3))
    ans = 0
    for c in comb:
        if isOver(c, acc):
            continue
        sum_w = c[0] * w1 + c[1] * (w1+1) + c[2] * (w1+2) + c[3] * (w1+3)
        if sum_w > W:
            continue
        res = 0
        for i in range(4):
            if c[i] == 0:
                continue
            res += acc[i][c[i]-1]
        
        ans = max(ans,res)
    
    print(ans)

def isOver(c, acc):
    res = False
    for i in range(4):
        if len(acc[i]) < c[i]:
            res = True
    
    return res
if __name__ == '__main__':
    solve()