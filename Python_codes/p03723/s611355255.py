# -*- coding:utf-8 -*-
A,B,C = map(int,input().split())

cnt = 0

if A==B==C==1:
    pass
elif A==B==C:
    cnt = -1
else:
    while A%2 == 0 and B%2 == 0 and C%2 == 0:
        A,B,C = (B+C)//2,(C+A)//2,(A+B)//2 
        cnt += 1

print(cnt)
