import sys
sys.setrecursionlimit(100000000)
n=int(input())
memo=[-1]*(10**7)
memo[0]=0
def rec(a:int):
    if a==0:
        return 0
    if memo[a]!=-1:
        return memo[a]
    res=100000
    for i in range(1,9):
        if 0<=a-6**i:
            res=min(res,rec(a-6**i)+1)
    for j in range(1,9):
        if 0<=a-9**j:
            res=min(res,rec(a-9**j)+1)
    res=min(res,rec(a-1)+1)

    memo[a] = res

    return res
print(rec(n))