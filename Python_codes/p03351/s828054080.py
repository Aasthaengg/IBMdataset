# coding: utf-8
a,b,c,d=map(int,input().split())

if abs(a-c)<=d:
    print("Yes")
else:
    if a<b<c and c-b<=d and b-a<=d:
        print("Yes")
    elif c<b<a and a-b<=d and b-c<=d:
        print("Yes")
    else:
        print("No")

