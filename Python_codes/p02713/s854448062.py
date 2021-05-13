# coding: utf-8
# Your code here!
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math
N=int(input())
count=0
for i in range(1,N+1):
    for j in range(1,N+1):
        s=math.gcd(i,j)
        for k in range(1,N+1):
            count+=math.gcd(s,k)
print(count)