A,B,C = (int(T) for T in input().split())
print(min(A+B,B+C,C+A))