n, a = [int(input()) for _ in range(2)]

rest = n - (n//500) * 500
if rest>a:
    print("No")
else:
    print("Yes")