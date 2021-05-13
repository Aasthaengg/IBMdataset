N, A, B = map(int, raw_input().split())
m=A+B
print min(A, B), max(0,m-N)