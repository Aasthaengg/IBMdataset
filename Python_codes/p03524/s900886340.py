s = input()

A = s.count("a")
B = s.count("b")
C = s.count("c")

if abs(A-B) < 2 and abs(A-C) < 2 and abs(B-C) < 2:
    print("YES")
else:
    print("NO")