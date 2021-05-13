n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n < k:
    ans = n * x
    print(ans)

else:
    ans = x * k + y * (n - k)
    print(ans)