# coding: utf-8
# Your code here!
import math

while True:
    n=int(input())
    
    if n==0:
        break
    else:
        S=[int(s) for s in input().split()]
        a2=0
        
        m=sum(S)/n
        
        for i in range(n):
            a2+=(S[i]-m)**2
            a=math.sqrt(a2/n)

    print(f'{a:.5f}')
