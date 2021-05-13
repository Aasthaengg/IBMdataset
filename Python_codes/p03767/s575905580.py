N = int(input())
a = sorted(list(map(int, input().split())))

print(sum(a[-2 * (i+1)] for i in range(N)))
