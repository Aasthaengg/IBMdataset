import sys
a, b, c = (int(i) for i in input().split())  
print(1 + min(a + b, c - 1) + b)
