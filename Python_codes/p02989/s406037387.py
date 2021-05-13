N = int(input())
d = list(map(int, input().split()))

d.sort()

result = d[int(N/2)] - d[int(N/2) - 1]

print(result)