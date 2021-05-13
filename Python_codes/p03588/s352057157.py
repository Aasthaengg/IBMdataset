N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]

AB.sort(key=lambda x: x[0])
l, r = AB[-1]

print(l + r)
