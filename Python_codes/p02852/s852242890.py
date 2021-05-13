import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
S = input()

rS = [i for i in reversed(S)]
res = []
step = 0

lenS = len(S)
while 1:
    if step == lenS-1:
        break
    for i in range(M, -1, -1):
        if step+i > lenS-1:
            continue
        if i == 0:
            print(-1)
            exit()
        if rS[step+i] == '0':
            step += i
            res.append(i)
            break

print(*reversed(res))
