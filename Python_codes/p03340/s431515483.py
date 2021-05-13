
N = int(input())

A = list(map(int,input().split()))


ans = 0

nows = 0
nowx = 0
l = 0

for r in range(N):

    nows += A[r]
    nowx ^= A[r]

    while nows != nowx:
        nows -= A[l]
        nowx ^= A[l]
        l += 1

    ans += r-l+1

print (ans)
