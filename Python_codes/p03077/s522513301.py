N = int(input())
A = [int(input()) for _ in range(5)]
a = min(A)
n = N//a
b = N%a
if b==0:
    print(5+n-1)
else:
    print(5+n)