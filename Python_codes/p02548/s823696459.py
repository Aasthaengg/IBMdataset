from bisect import bisect_right

N = int(input())
num = [i for i in range(1, N)]
cnt = 0
for a in range(1, N):
    n = (N - 1) // a
    b = bisect_right(num, n)
    cnt += b

print(cnt)
