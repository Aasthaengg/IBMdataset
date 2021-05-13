#5814544

from bisect import bisect_left

N,Q = map(int,input().split())

STX = []
D = []
for _ in range(N):
    STX.append(list(map(int,input().split())))
for _ in range(Q):
    D.append(int(input()))

STX.sort(key=lambda x:x[2])

ans = [-1]*Q
skip = [-1]*Q

for s,t,x in STX:
    left = bisect_left(D,s-x)
    right = bisect_left(D,t-x)

    while left < right:
        if skip[left] == -1:
            ans[left] = x
            skip[left] = right
            left += 1
        else:
            left = skip[left]
    
for a in ans:
    print(a)