N = int(input())
d = sorted(map(int, input().split()))

print(d[int(N/2)] - d[int(N/2-1)])