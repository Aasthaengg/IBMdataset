N = int(input())
buttons = [int(input()) for i in range(N)]

cur = 1
for i in range(N):
    cur = buttons[cur-1]

    if cur == 2:
        print(i+1)
        exit()

print(-1)