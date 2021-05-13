import sys

read = sys.stdin.read

N, H, W, *AB = map(int, read().split())
answer = 0
for a, b in zip(*[iter(AB)] * 2):
    if H <= a and W <= b:
        answer += 1

print(answer)
