import sys
input = sys.stdin.buffer.readline

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab = sorted(ab, key=lambda x:x[0])
print(ab[-1][0] + ab[-1][1])
