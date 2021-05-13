N = int(input())
LP = list(map(int, input().split()))

LPS = []
LPS = sorted(LP)

cnt = 0
for i in range(N):
    if LP[i] != LPS[i]:
        cnt += 1
        if cnt == 3:
            print("NO")
            exit()

print("YES")