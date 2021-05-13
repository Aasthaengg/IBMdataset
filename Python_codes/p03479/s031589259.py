import sys
sys.setrecursionlimit(10000)

x,y = map(int,input().split())


if y == x:
    print(1)
    exit()

asn = 0
def dfs(x,y,n):
    
    n += 1
    ans = x*2**n
    if ans > y:
        return n
    else:
        return dfs(x,y,n)

a = dfs(x,y,1)

print(a)