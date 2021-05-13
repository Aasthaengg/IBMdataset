import math

while(1):
    a_2 = 0
    n = int(raw_input())
    if n == 0:
        break
    s = map(float, raw_input().split())

    Sum = sum(s)
    m = Sum/n
    
    for i in range(n):
        a_2 += (s[i] - m)**2 
    a_2 = a_2/n
    
    a = math.sqrt(a_2)
    
    print a