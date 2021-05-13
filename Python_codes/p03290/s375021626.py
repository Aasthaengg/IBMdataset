from itertools import groupby, accumulate, product, permutations, combinations
def solve():
    ans = float('inf')
    D, G = map(int, input().split())
    P = [0]*D
    C = [0]*D
    for i in range(D):
        P[i],C[i] = map(int, input().split())
    for p in product([0,1],repeat=D):
        cnt = 0
        num = 0
        for i in range(D):
            if p[i]==1:
                cnt += 100*(i+1)*P[i]+C[i]
                num += P[i]
        if cnt<G:
            for i in range(D-1,-1,-1):
                if p[i]==0:
                    if (G-cnt+100*i)//(100*(i+1))<P[i]:
                        num += (G-cnt+100*i)//(100*(i+1))
                        break
            else:
                continue
        ans = min(ans,num)
    return ans
print(solve())