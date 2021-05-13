line = input()
A, B, X = [int(n) for n in line.split()]
if X < A or X > B+A:
    print("NO")
else:
    print("YES")