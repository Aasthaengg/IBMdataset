import sys
N = int(input())
L = list(map(int, input().split()))
cnt = 1
if 0 in L:
    print(0)
    sys.exit()
for i in range(N):
    cnt *= L[i]
    if cnt > 10**18:
        print(-1)
        sys.exit()
print(cnt)
