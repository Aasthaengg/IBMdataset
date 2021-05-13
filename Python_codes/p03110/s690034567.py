n = int(input())
c = 0
for i in range(n):
    x, u = input().split()
    if u == "JPY":
        c += int(x)
    else:
        c += float(x) * 380000.0
print(c)