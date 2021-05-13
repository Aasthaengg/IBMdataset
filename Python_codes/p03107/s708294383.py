import math
from collections import defaultdict
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""
s=ip()
a=s.count('1')
b=s.count('0')
print(min(a,b)*2)
