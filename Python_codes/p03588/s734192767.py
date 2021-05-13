n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()
print(ab[-1][0]+ab[-1][1])