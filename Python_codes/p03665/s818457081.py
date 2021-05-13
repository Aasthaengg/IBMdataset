import math
 
def combination(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)    

N,P = map(int,input().split())

A = list(map(int,input().split()))

kisu = 0
gusu = 0

for a in A:
    if a%2 == 0:
        gusu += 1
    else:
        kisu += 1

sum_gu = 2**gusu

if P%2==0:
    sum_ki = 0
    for i in range(2,kisu+1, 2):
        sum_ki += combination(kisu, i)
    sum_ki *= sum_gu
    print(sum_gu+sum_ki)
else:
    sum_ki = 0
    for i in range(1,kisu+1, 2):
        sum_ki += combination(kisu, i)
    print(sum_gu*sum_ki)