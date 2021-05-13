n,k = map(int, input().split())
A = list(map(int,input().split()))

def gcd(a,b):
    r = 1
    while r!=0:
        r = a%b
        a = b
        b = r
    return a

if max(A)<k:
    print('IMPOSSIBLE')
    exit()

if max(A)==n or min(A)==1:
    print('POSSIBLE')
    exit()

ans = A[0]
for i in A:
    ans = gcd(ans,i)

if ans > 1:
    if gcd(ans,k)>1:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

else:
    print('POSSIBLE')
