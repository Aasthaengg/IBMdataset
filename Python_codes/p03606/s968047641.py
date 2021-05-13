import sys
input = sys.stdin.buffer.readline

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for l, r in LR:
  answer += r - l + 1

print(answer)