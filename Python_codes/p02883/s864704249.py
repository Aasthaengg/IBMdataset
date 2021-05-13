N,K = list(map(int,input().split()))

A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort()
F.sort(reverse=True)

def check(v):
    ans = 0
    for i in range(N):
        ans += max(A[i] - v//F[i],0)
    return ans<=K

if check(0):
    print(0)
else:
    l = 0
    r = 10**12 + 1
    while r-l>1:
        if check((l+r)//2):
            r = (l+r)//2
        else:
            l = (l+r)//2
    print(r)