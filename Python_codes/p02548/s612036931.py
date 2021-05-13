from collections import Counter
import math
import statistics
import itertools
a=int(input())
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
# A,B,C= map(int,input().split())
# f = list(map(int,input().split()))
# g = [input() for _ in range(a)]
count=0
for i in range(1,a):
    count+=(a-1)//i
print(count)