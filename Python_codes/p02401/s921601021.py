# coding: utf-8
# Your code here!
while(1):
    a,op,b=input().split(" ")
    a=int(a)
    b=int(b)

    if op=="?":
        break
    if op=="+":
        print(int(a+b))
    if op=="-":
        print(int(a-b))   
    if op=="*":
        print(int(a*b))
    if op=="/":
        print(int(a/b))        
        
