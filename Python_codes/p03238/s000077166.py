import sys
N = int(input())
if not (N == 1 or N == 2):
    sys.exit()

if N == 1:
    print('Hello World')  
elif N == 2:
    A = int(input())
    B = int(input())
    print(A+B)