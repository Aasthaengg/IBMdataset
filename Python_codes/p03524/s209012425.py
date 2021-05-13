s = input()

a = s.count("a")
b = s.count("b")
c = s.count("c")

mx = max(a, b, c)
mn = min(a, b, c)

if mx - mn > 1:
    print("NO")
else:
    print("YES")