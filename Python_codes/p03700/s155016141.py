
def updiv(a,b):

    if a % b == 0:
        return a // b
    else:
        return a // b + 1

def able(n):

    nt = 0
    for i in range(N):
        if h[i] - B*n <= 0:
            continue
        nt += updiv(h[i] - B*n , A-B)
        #print (h[i],B,h[i]-B*n,A-B,nt)

    if nt <= n:
        return True
    else:
        return False

N,A,B = map(int,input().split())

h = []
for i in range(N):
    H = int(input())
    h.append(H)

l = 0
r = max(h)
lf = able(l)
rf = able(r)

while r - l != 1:

    m = (l + r) // 2
    mf = able(m)

    if not mf:
        l = m
        lf = mf
    else:
        r = m
        rf = mf

print (r)
