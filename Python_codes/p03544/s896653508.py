n = int(input())
a = 2
b = 1
if n == 1:
    print(1)
else:
    for i in range(2,n+1):
        ans = a + b
        a = b
        b = ans
    print(ans)