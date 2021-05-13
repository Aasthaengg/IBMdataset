from bisect import bisect_right, bisect_left
n = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

ans = 0
for b in B:
    a_id = bisect_left(A, b)
    c_id = bisect_right(C, b)
    ans += a_id * (len(C) - c_id)

print(ans)