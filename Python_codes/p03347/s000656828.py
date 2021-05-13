n = int(input())
a = [int(input()) for i in range(n)]

if a[0]!=0:
    print(-1)
    exit()

ans = a[-1]
x = a[-1]
for i in range(n-1):
    if a[-i-2] > x-1:
        ans += a[-i-2]
        x = a[-i-2]
    elif a[-i-2]==x-1:
        x -=1
    else:
        print(-1)
        exit()

print(ans)