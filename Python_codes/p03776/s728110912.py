from scipy.misc import comb
N,A,B = map(int,input().split())
v = list(map(int,input().split()))
v.sort(reverse=True)

ans = 0
if v[A-1] == v[0]:
    mean = v[0]
    count = 0
    for i in range(N):
        if v[i] == v[0]:
            count += 1
    for i in range(A,min(B,count)+1):
        ans += comb(count,i,exact=True)
else:
    mean = sum(v[:A])/A
    count = 0
    j = N
    for i in range(N):
        if v[i] == v[A-1]:
            j = min(i,j)
            count += 1
    ans = comb(count,A-j,exact=True)
print(mean)
print(ans)