from bisect import bisect_right, bisect_left

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0

for bi in range(N):
    ai_max = bisect_left(A, B[bi])
    ci_min = bisect_right(C, B[bi])
    ans += (ai_max) * (N - ci_min)

print(ans)
