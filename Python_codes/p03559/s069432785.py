from bisect import bisect_right, bisect_left

N = int(input())

As = sorted(list(map(int, input().split())))
Bs = sorted(list(map(int, input().split())))
Cs = sorted(list(map(int, input().split())))

ans = 0

for B in Bs:
    A_idx = bisect_left(As, B)
    C_idx = bisect_right(Cs, B)
    ans += A_idx * (N - C_idx)

print(ans)