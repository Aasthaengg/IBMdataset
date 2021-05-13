
n=int(input())
s=input()
if n%2==1:
    print("No")
    exit()
a=s[0:len(s)//2] 
b=s[len(s)//2 if len(s)%2 == 0 else ((len(s)//2)+1):]

if a.__eq__(b):
    print("Yes")
    exit()
else:
    print("No")