n = int(input())
n_100 = n // 100
n_1 = n % 10
if n_100 == n_1:
    print("Yes")
else:
    print("No")