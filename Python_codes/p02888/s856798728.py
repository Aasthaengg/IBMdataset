import bisect
N = int(input())
L = list(map(int,input().split()))
L.sort()

cnt = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        num = L[i] + L[j]
        third = bisect.bisect_left(L,num)
        if third > j:
            cnt += third - j - 1
print(cnt)