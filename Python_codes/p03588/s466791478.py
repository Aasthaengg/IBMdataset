n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

print((ab[0][0]-1) + (ab[-1][1]-0) + (ab[-1][0]-ab[0][0]+1))