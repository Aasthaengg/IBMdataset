N = int(input())
d = list(map(int, input().split()))

d.sort()
n = N // 2

print(d[n:][0] - d[:n][-1])