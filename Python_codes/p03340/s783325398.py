from itertools import accumulate
N = int(input())
A = list(map(int,input().split()))

l = 0
r = 1
tmp = A[0]
ans = 0
while l<N:
    if r==N:
        ans += r-l
        l += 1
    elif tmp+A[r] == tmp^A[r]:
        tmp = tmp+A[r]
        r += 1
    else:
        ans += r-l
        tmp = tmp-A[l]
        l += 1
print(ans)