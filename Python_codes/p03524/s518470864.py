S = input()
x = (S.count("a"), S.count("b"), S.count("c"))

if max(x) - min(x) >= 2:
    print("NO")
else:
    print("YES")
