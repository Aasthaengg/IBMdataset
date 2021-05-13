from math import sqrt

while True:
    n = int(input())
    if n == 0:
        break
    
    lst = list(map(float,input().split()))
    ave = sum(lst) / len(lst)
    alpha = 0.0
    for i in lst:
        alpha += (ave - i)**2
    S = sqrt((alpha/n))
    print(S)
