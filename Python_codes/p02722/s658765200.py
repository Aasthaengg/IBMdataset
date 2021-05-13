import math

n = int (input())
sqr = int (math.sqrt(n))
ans = 1 # n itself

def check (x) :
    tmp = n
    while (tmp % x == 0) :
        tmp /= x
    return True if tmp % x == 1 else False

for i in range (2, sqr + 1) :
    if (n % i == 0) :
        if (check (i)) :
            ans += 1
        if (i != n / i and check (n / i)) :
            ans += 1
    
m = n - 1
if (m > sqr) :
    ans += 1 # m
    for i in range (2, sqr + 1) :
        if (m % i == 0) :
            ans += 1 
            if (i != m / i) :
                ans += 1

print (ans)