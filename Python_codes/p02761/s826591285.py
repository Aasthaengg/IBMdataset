import sys


def LI():
    return list(map(int, input().split()))


N, M = LI()
ans = [-1]*N
for _ in range(M):
    a, b = LI()
    if ans[a-1] == b or ans[a-1] == -1:
        ans[a-1] = b
    else:
        print(-1)
        sys.exit()
if ans[0] == -1:
    if N==1:
        print(0)
        sys.exit()
    ans[0] = 1
if ans[0] == 0:
    if N == 1:
        print(0)
    else:
        print(-1)
    sys.exit()
S = ""
for i in range(N):
    if ans[i] == -1:
        ans[i] = 0
    S += str(ans[i])
print(S)
