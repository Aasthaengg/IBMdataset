
A, B = map(int, input().split())

print(A+B if A==B else max(A, B)+ max(A-1, B-1))
