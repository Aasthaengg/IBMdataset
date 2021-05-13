import math
n = int(input())
l = int(math.log10(n))
ma = n//10**l
ans = ma+l*9
#print(str(ma)+'9'*l,n)
if int(str(ma)+'9'*l) > n:
    print(ans-1)
else:
    print(ans)