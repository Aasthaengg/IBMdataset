N = int(input())

ans = 1
for i in range(101):
    if (ans * 2  > N):
        print(ans)
        exit()
    else:
        ans *= 2