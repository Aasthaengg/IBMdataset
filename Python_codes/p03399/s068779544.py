import sys
input = sys.stdin.readline
ABCD = [int(input()) for _ in range(4)]
sum = 0
sum += min(ABCD[:2])
sum += min(ABCD[2:])
print(sum)