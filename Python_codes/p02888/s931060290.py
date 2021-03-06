from bisect import bisect_left, bisect_right

n = int(input())
stick = list(map(int, input().split()))
stick.sort()

count = 0
for i in range(n):
    for j in range(i + 1, n):
        l = bisect_left(stick, stick[j] - stick[i] + 1)
        r = bisect_right(stick, stick[i] + stick[j] - 1) - 1
        if r < 0 or l >= n:
            break
        count += r - l + 1
        if l <= i <= r:
            count -= 1
        if l <= j <= r:
            count -= 1
print(count // 3)