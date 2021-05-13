a, b = list(map(str, input().split()))
p = a + b
p1 = list(set(p))
if len(p1) == 1:
    print("H")
else:
    print("D")