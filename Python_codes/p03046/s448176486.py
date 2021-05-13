import sys
# input = sys.stdin.readline
inf = 10 ** 18

M, K = map(int, input().split())

tmp = 0
notK = []
for i in range(1 << M):
    if i == K: continue
    tmp ^= i
    notK.append(i)
if K == 0:
    ans = []
    for i in range((1 << M)):
        ans.append(i)
    for i in range((1 << M)):
        ans.append((1 << M) - 1 - i)
    #
    for i, ansi in enumerate(ans):
        if i > 0: print(' ', end='')
        print(ansi, end='')
    print()
elif tmp != K:
    print(-1)
else:
    ans = []
    ans.append(notK[0])
    ans.append(K)
    ans.append(notK[0])
    for i in range(1, (1 << M) - 1):
        ans.append(notK[i])
    ans.append(K)
    for i in range(1, (1 << M) - 1):
        ans.append(notK[(1 << M) - 1 - i])
    #
    for i, ansi in enumerate(ans):
        if i > 0: print(' ', end='')
        print(ansi, end='')
    print()