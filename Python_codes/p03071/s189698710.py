A, B = map(int, input().split())
max(A,B) + max((max(A,B) -1), min(A,B))
print(max(A,B) + max((max(A,B) -1), min(A,B)))