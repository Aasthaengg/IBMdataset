from bisect import bisect_left, bisect_right

n = int(input())
stick = list(map(int, input().split()))
stick.sort()

count = 0
for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        l = bisect_left(stick, stick[i] - stick[j] + 1)
        r = bisect_right(stick, stick[i] + stick[j] - 1) - 1
        if j <= l or l > r:
            break
        count += min(r + 1, j) - l
print(count)

