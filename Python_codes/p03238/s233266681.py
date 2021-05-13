import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

if N == 1:
    print("Hello World")
else:
    A = int(input())
    B = int(input())    
    print(A+B)