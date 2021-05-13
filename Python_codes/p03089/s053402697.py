from collections import deque

N = int(input())
B = [int(i) for i in input().split()]

if B[0] != 1:
    print(-1)
    exit()
if N == 1:
    print(1)
    exit()

# B[0]は絶対1だから後で加える
B.pop(0)

ans = deque()
while B:
    tmp = -1
    for i,b in enumerate(B):
        if i == 0 and b == 1:
            tmp = i
        elif b == i + 2:
            tmp = i
    if tmp < 0:
        print(-1)
        exit()
    ans.appendleft(B.pop(tmp))

ans.appendleft(1)

print(*ans, sep="\n")