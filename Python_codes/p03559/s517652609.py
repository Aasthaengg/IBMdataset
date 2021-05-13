import bisect

n = int(input())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

sum = 0
for i in range(len(b)):
    ai = bisect.bisect_left(a, b[i])
    ci = bisect.bisect_right(c, b[i])
    sum += ai * (n - ci)

print(sum)