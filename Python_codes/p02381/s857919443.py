from math import sqrt

while True:
    n = int(input().strip())    
    if n == 0:
        break    
    scores = list(map(float, input().strip().split()))
    sum1 = 0 
    for i in scores:
        sum1 += i
    heikin = sum1 * 1 / n
    sum2 = 0
    for i in scores:
        sum2 += (i - heikin) ** 2
    a = sqrt(sum2 / n)
    print(a)
    

    

