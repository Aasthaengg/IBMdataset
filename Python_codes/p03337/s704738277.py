A, B = (int(x) for x in input().split())
print(max(max(A+B, A-B), A*B))