# coding: utf-8
import math
#n = int(input())
#x, y = map(int,input().split())
#A = list(map(int,input().split()))
ans = 0
s = input()
n = len(s)
s=s[::-1]
i=0
flg=True
while True:
    if i>=n:
        break
    if s[i:i+7]=="remaerd":
        i+=7
    elif s[i:i+6]=="resare":
        i+=6
    elif s[i:i+5]=="maerd" or s[i:i+5]=="esare":
        i+=5
    else:
        flg=False
        break
if flg:
    print("YES")
else:
    print("NO")