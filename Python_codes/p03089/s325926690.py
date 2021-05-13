import sys

N = int(input())
B = list(map(int, sys.stdin.readline().rsplit()))

res = []
for _ in range(N):
    tmp = -1
    for i, b in enumerate(B):
        if i + 1 == b:
            tmp = i
    if tmp == -1:
        print(-1)
        exit()
    res.append(B.pop(tmp))

print("\n".join(map(str, res[::-1])))
