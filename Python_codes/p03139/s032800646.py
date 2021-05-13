N, A, B = map(int, input().split())
both = min(A, B)
none = 0 if A+B-N<0 else A+B-N
print(both, none)