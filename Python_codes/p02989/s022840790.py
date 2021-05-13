N = int(input())
d = list(map(int, input().split()))
d = sorted(d)

x = d[N//2 - 1]
y = d[N//2]

print(0 if x == y else y-x)
