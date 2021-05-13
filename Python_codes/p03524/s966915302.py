s = input()

A = s.count("a")
B = s.count("b")
C = s.count("c")

if max(A,B,C) - min(A,B,C) <= 1:
    print("YES")
else:
    print("NO")