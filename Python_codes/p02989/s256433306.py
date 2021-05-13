N = int(input())
d = list(map(int, input().split()))

d = sorted(d)
print(d[int(N/2)] - d[int(N/2) - 1])