N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = sum(a)
B = sum(b)

# 最大試行回数
n = B - A
r_a = 0
r_b = 0
cnt = 0

for i, j in zip(a, b):
    if i < j:
        if (j - i) % 2 == 1:
            if r_b:
                r_b -= 1
            else:
                cnt += 1
                r_a += 1
            j += 1
        d = (j - i) // 2
        if d <= r_a:
            r_a -= d
        else:
            d -= r_a
            r_a = 0
            cnt += d
            r_b += d
    elif i > j:
        d = i - j
        if d <= r_b:
            r_b -= d
        else:
            d -= r_b
            r_b = 0
            cnt += d
            r_a += d

if cnt <= n:
    print('Yes')
else:
    print('No')
