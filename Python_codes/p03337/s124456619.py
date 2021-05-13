IN = [int(_) for _ in input().split()]
A = IN[0]
B = IN[1]

print(max(A+B,A-B,A*B))