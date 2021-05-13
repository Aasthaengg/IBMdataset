n, m = map(int, input().split(" "))
a = map(int, input().split(" "))

z = n - sum(a)

print(z if z >=0 else -1)