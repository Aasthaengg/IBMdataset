N = int(input())
D = list(map(int, input().split()))
SD = sorted(D)
m = N // 2
print(SD[m] - SD[m - 1])
