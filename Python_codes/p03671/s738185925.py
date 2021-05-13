A, B, C = list(map(int, input().split()))
print(min(A+B, B+C, C+A))