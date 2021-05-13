from bisect import bisect_left, bisect_right

n = int(input())
stick = list(map(int, input().split()))
stick.sort()

count = 0
for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        l = bisect_right(stick, stick[i] - stick[j])
        r = bisect_left(stick, stick[i] + stick[j]) # [l, r) が範囲
        if j <= l:
            break
        count += min(r, j) - l
print(count)

