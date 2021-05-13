n = int(input())
otoshidama = []
for i in range(n):
    x, u = input().split()
    x = float(x)
    if u == "JPY":
        otoshidama.append(x)
    else:
        otoshidama.append(x*380000)
ans = sum(otoshidama)
print(f"{ans:.5f}")
