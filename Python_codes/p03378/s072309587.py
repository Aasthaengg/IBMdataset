import bisect

x = int(input().split()[2])
a = list(map(int, input().split()))
i = bisect.bisect(a, x)

print(min(i, len(a) - i))