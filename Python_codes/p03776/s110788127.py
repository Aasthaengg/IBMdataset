from collections import Counter
def cmb(n,k):
    over = 1
    under = 1
    for i in range(n-k+1,n+1):
        over *= i
    for i in range(1,k+1):
        under *= i
    return over//under

N,A,B = map(int,input().split())
v = list(map(int,input().split()))
C = Counter(v)
li = sorted(list(C.keys()),reverse=True)
ans = 0
SUM = 0
ave = 0
remain = A
n = C[li[0]]
if n >= A:
    ave = li[0]
    for k in range(A,min(B,n)+1):
        ans += cmb(n,k)
else:
    for i in li:
        if C[i] < remain:
            SUM += i*C[i]
            remain -= C[i]
        else:
            SUM += i*remain
            ans = cmb(C[i],remain)
            ave = SUM/A
            break
print(ave)
print(ans)