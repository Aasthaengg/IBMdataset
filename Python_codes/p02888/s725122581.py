from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
#print(L)
ans = 0

"""
これだとTLEしてしまう
for i in range(N-2):
    for j in range(i+1, N-1):
        left = j
        right = N
        target = L[i]-L[j]
        while right-left > 1:
            mid = (right + left)//2
            #print(mid)

            if L[mid] > target:
                left = mid
            else:
                right = mid

        ans += left-j
        """

L.sort()
for i in range(N):
    for j in range(i+1, N):
        target = L[i]+L[j]
        left = bisect_left(L, target) #二分探索の関数
        ans += max(0, left-j-1)


print(ans)
