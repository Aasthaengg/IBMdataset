from bisect import bisect_right,bisect_left
N = int(input())
L = sorted(list(map(int,input().split())))
cnt = 0
for i in range(N-1):
    for j in range(i+1,N):
        a = L[i]
        b = L[j]
        indU = bisect_left(L,a+b)
        indL = bisect_right(L,b-a)
        if j<indU and i>= indL:
            cnt += indU-indL-2
        elif indL<=i<indU and j>=indU or i<indL and indL<=j<indU:
            cnt += indU-indL-1
        elif j<indL or i>=indU:
            cnt += indU-indL
print(cnt//3)