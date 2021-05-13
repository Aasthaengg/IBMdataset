n, x = map(int, input().split())
A = list()
for i in range(n):
    a = int(input())
    x -= a 
    A.append(a)
A.sort()
if x == 0:
    print(n)
else :
    b = x//A[0]
    print(n+b)
