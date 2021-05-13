N, A, B = map(int, input().split())
V = list(map(int, input().split()))

def comb(n,r):
    ans = 1
    for i in range(r):
        ans *= n-i
    for i in range(r):
        ans //= i+1
    return ans

V.sort(reverse=True)
print(sum(V[:A])/A)

def solve(V,A,B):
    if V[A-1]>V[A]:
        return 1
    a = V[A-1]
    l,r = -1,-1
    for i in range(N):
        if l==-1 and V[i]==a:
            l = i
        if r==-1 and V[i]<a:
            r = i
    if r==-1:
        r = N
    lower = A-l
    upper = min(r,B)-l
    total = r-l
    ans = 0
    if V[0]==a:
        for i in range(lower,upper+1):
            ans += comb(total,i)
    else:
        ans += comb(total,lower)
    return ans
print(solve(V,A,B))