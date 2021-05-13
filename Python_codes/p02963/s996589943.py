S = int(input())
m = S // (10**9)
n = S % (10**9)

p,q = 0,0
r,s = 0,0
if(m == 10**9):
    p,q = 10**9,1
    r,s = 0,10**9
else:
    p,q = m+1,10**9-n
    r,s = 1,10**9
print(0,0,p,q,r,s)