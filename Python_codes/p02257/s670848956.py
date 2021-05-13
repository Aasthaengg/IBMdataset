def isprime(x):
    import math
    if  x == 2:
        return True
    elif x < 2 or x % 2 == 0:
        return False
    else:
        i = 3
        while i <= math.sqrt(x):
            if x % i == 0:
                return False
            i += 2
        return True

N = int(input())
A=[]
for i in range(N):
    A.append(int(input()))
counter = 0
for i in range(0, N):
    if isprime(A[i]):
        counter += 1
        
print(counter)