import math
A,B,C = map(int,input().split())
num = math.gcd(math.gcd(A,B),C)
A = A//num
B = B//num
C = C//num
for i in range(1,100000):
    if (A*i)%B == 1:
        print('YES')
        exit()
print('NO')