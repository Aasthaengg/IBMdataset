N,A,B = map(int, input().split())
H = [int(input()) for _ in range(N)]


def f(n, H, A, B): #n回の爆発で魔物を全て倒せるか判定
    c = 0
    for i in range(len(H)):
        t = H[i]
        t -= B*n
        if t > 0:
            c += t//(A-B) + min(1, t%(A-B))
    if c > n:
        return False
    else:
        return True
    
    
def g(u, l, H, A, B): #魔物を倒すことができる爆発の最小回数を二分探索
    if u-l < 2:
        if f(l, H, A, B):
            return l
        else:
            return u
    m = (u+l)//2
    if f(m, H, A, B):
        return g(m, l, H, A, B)
    else:
        return g(u, m, H, A, B)
    
    
ans = g(10**9, 1, H, A, B)
print(ans)