A, B, C = [int(n) for n in input().split()]
print(C if A*C <= B else B//A) 