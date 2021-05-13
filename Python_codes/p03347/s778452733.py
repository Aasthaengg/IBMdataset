n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
if a[0] != 0:
    ans = -1
elif n == 1:
    ans = 0
else:
    b = a[1:]
    for k,i in enumerate(b):
        if i <= 1:
            ans += i
        else:
            num = i-a[k]
            if num == 1:
                ans += 1
            elif num <= 0:
                ans += i
            else:
                ans = -1
                break
print(ans)