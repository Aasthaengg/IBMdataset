a, b, c = map(int, input().split())
x = a*b*c
A, B, C = a//2*b*c, b//2*a*c, c//2*a*b
print(min(abs(2*A-x), abs(2*B-x), abs(2*C-x)))