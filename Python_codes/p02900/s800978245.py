import math

def isprime(n):
    if(n == 1):
        return True
    if(n == 2):
        return True
    if(n%2 == 0):
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if(n%i == 0):
            return False
        
    return True

def yakusuu(n):
    l = []
    u = []
    i = 1
    while(i*i <= n):
        if(n%i == 0):
            l.append(i)
            if(i != n//i):
                u.append(n//i)
        i += 1
    return l+u[::-1]
        
A, B = map(int, input().split())
a = set(yakusuu(A))
b = set(yakusuu(B))

lst = []
for i in a:
    if(i in b):
        lst.append(i)
   
cnt = 0
for i in range(len(lst)):
    if(isprime(lst[i])):
        cnt += 1
    
print(cnt)