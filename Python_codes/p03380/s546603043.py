from bisect import bisect_left

n = int(input())
A = list(int(x) for x in input().split())
m = max(A)
A.remove(m)
A.sort()
index = bisect_left(A, m//2)
tmp = 10**18
ans = -1
for a in A[index-1:index+2]:
    if abs(a - m/2) < tmp:
        tmp = abs(a - m/2)
        ans = a
print(m, ans)