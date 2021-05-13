n = int(input())
if n == 10 or n == 10 ** 2 or n == 10 ** 3 or n == 10 ** 4 or n == 10 ** 5:
    print(10)
else:
    ans = 0
    a = str(n)
    for i in range(len(a)):
        ans += int(a[i])
    print(ans)