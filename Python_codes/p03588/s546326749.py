N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
sAB = sorted(AB, key=lambda x: - x[0])
print(sum(sAB[0]))