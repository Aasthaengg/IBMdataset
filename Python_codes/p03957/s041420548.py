# coding: utf-8
s=input()
n=len(s)
flg=False
flg_=False
a=0
b=0
for i in range(n):
    if s[i]=="C":
        a=i
        flg=True
        break
for i in range(n-1,-1,-1):
    if s[i]=="F":
        b=i
        flg_=True
        break
if flg and flg_ and a<b:
    print("Yes")
else:
    print("No")