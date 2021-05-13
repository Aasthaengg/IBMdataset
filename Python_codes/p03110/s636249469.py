ii = lambda:int(input())
mi = lambda:list(map(int,input().split()))
ix = lambda x:list(input() for _ in range(x))
mix = lambda x:list(mi() for _ in range(x))
iix = lambda x:list(int(input()) for _ in range(x))
##########
def main(n,l):
    res = 0
    for x,u in l:
        res += calc(x,u)
    return res
    
def calc(x,u):
    return int(x) if u == "JPY" else float(x) * 380000

n = ii()
l = list([input().split() for _ in range(n)])
print(main(n,l))