N, P = map(int,input().split())
A = list(map(int,input().split()))
even = 0
odd = 0

for i in A:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
#print(even,odd)

import math
def Perm(n, r):
    return math.factorial(n)//math.factorial(n-r)
def comb(n, r):
    return Perm(n, r)//math.factorial(r)

#print("0,0 = ", comb(0,0))

if P == 0:
    ans = 0
    for x in range(odd+1):
        #print(odd, x)
        if x % 2 == 0:
            ans += comb(odd,x)
    ans *= 2**even
    print(ans)
else:
    ans = 0
    for x in range(odd+1):
        if x % 2 == 1:
            if odd != 0:
                ans += comb(odd,x)
    ans *= 2**even
    print(ans)