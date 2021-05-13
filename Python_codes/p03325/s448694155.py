import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

res = 0
for a in A:
    while True:
        if a % 2 == 1:
            break
        else:
            a //= 2
            res += 1

print(res)
