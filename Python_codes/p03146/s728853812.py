def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1
s = int(input())
A = [s]
for i in range(2, 1000001):
    A.append(f(A[-1]))
    if len(A) != len(set(A)):
        print(i)
        exit(0)