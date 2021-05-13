A,B = map(int, input().split())

print(A+B if A == B else 2*max(A, B) -1)
