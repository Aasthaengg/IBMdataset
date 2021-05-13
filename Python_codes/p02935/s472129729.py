N = int(input())
v = sorted(list(map(int, input().split())))

ave = (v[0] + v[1]) / 2
for i in range(1, N - 1):
    ave = (ave + v[i + 1]) / 2
print(ave)
