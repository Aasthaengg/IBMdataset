line = input()
A,B = [int(u) for u in line.split()]
print(max(A+B,A-B,A*B))