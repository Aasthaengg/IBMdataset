N = int(input())
A = int(input())
if N > 1000:
    N = N%1000
if N <= A:
    print("Yes")
else:
    print("No")