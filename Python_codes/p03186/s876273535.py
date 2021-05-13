A, B, C = map(int, input().split())

if C > A + B + 1:
  C = A + B + 1
  
print(B + C)