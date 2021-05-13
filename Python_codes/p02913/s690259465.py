N = int(input())
S = input()
def f(m):
    res = False
    hs = []
    for i in range(0,N-m+1):
        hs.append(hash(S[i:i+m]))
    for i in range(0,N-m+1):
        if hash(S[i:i+m]) in hs[i+m:]:
            res = True
            break
    return res

l = 0
r = N//2+1
while (r-l)>1:
    mid = (r+l)//2
    if f(mid):
        l = mid
    else:
        r = mid
print(l)