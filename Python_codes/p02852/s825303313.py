import sys

stdin = sys.stdin
 
ni = lambda:int(ns())
na = lambda:list(map(int,stdin.readline().split()))
ns = lambda:stdin.readline().rstrip()  # ignore trailing spaces

N, M = na()
S = ns()

answer = [] # 後ろからできるだけ遠くに行く
S = S[::-1]
cur = 0
while cur < N:
    for i in range(M, 0, -1):
        if cur+i <= N and S[cur+i] == '0':
            answer.append(i)
            cur += i
            break
    else:
        print(-1)
        exit()
print(*answer[::-1])