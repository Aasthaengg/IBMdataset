# B
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]

ab.sort(reverse=True)
print(ab[0][0] + ab[0][1])