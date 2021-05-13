N, A, B = map(int, input().split())
print(min(A,B), end = " ")
print(max(0, A+B-N))