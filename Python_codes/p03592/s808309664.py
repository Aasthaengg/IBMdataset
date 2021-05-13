# coding: utf-8
n, m, k = map(int,input().split())
flg=False
for i in range(n+1):
    for j in range(m+1):
        if i*m + (n-i)*j - i*j == k:
            flg=True
if flg:
    print("Yes")
else:
    print("No")