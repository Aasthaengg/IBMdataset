n,a,b = map(int,input().split())
H = [int(input()) for i in range(n)]

lo = -1
hi = 10**9+1

while hi-lo > 1:
    mi = (hi+lo)//2
    rest = 0
    for i in range(n):
        rest += max(0,-(-(H[i]-b*mi)//(a-b)))
    if rest <= mi:
        hi = mi
    else:
        lo = mi
        
print(hi)