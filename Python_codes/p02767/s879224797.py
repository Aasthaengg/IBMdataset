n = int(input())
lst = list(map(int,input().split()))
for j in range(101):
    if (j == 0):
        ans = 0
        for i in range(n):
            ans = ans + lst[i]**2
    else:
        x = 0
        for i in range(n):
            x = x + (lst[i] - j)**2
        if (x < ans):
            ans = x

print(ans)
