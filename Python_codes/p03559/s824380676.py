from bisect import bisect_left, bisect_right
N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
A.sort()
B.sort()
C.sort()
ans = 0
for i in range(N):
    x = bisect_left(A,B[i])
    y = bisect_right(C,B[i])
    ans += x*(N-y)
print(ans)