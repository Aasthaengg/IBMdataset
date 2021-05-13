a = list(input())

n = a.count("0")
m = a.count("1")

print(min(n, m) * 2)