S = list(input())
a = S.count("a")
b = S.count("b")
c = S.count("c")

mi = min(a, b, c)
a -= mi
b -= mi
c -= mi
if a > 1 or b > 1 or c > 1:
    print("NO")
else:
    print("YES")
