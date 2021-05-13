N = int(input())
As = [int(input()) for i in range(N)]

if As[0] != 0:
    # 不可能
    print(-1)
    exit()

ans = 0
for i in reversed(range(1, N)):
    if As[i - 1] + 1 < As[i]:
        # 不可能
        ans = -1
        break
    elif As[i - 1] + 1 == As[i]:
        # X[i-1]→X[i]の、1回の操作で可能
        ans += 1
    else:
        # X[i-As[i]]から順に、As[i]回の操作が必要
        ans += As[i]

print(ans)
