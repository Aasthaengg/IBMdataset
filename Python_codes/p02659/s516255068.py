import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''
from decimal import Decimal
a,b= input().split()
a=int(a)
b=int(Decimal(b)*100)

print(a*b//100)