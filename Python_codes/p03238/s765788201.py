n = int(input())

if n == 1:
    ans = "Hello World"
else:
    a, b = [int(input()) for _ in range(2)]
    ans = a + b

print(ans)
