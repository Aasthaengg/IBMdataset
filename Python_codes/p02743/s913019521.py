# coding: utf-8
# Your code here!

def LI():
    return list(map(int,input().split()))

from decimal import Decimal

a,b,c=map(Decimal,input().split())

if a.sqrt()+b.sqrt()<c.sqrt():
    print("Yes")
else:
    print("No")