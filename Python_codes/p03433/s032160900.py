n, a = map(int, [input() for i in range(2)])

if n-500*(n//500) <= a:
    print("Yes")
else:
    print("No")