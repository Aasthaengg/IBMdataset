import sys

s = list(input())
k = int(input())

if len(s)==1:
    if k==1:
        print(0)
    else:
        print(k//2)
    sys.exit()  

x = 0
while True:
    if s[x]!=s[x+1]:
        break
    x += 1
    if x == len(s)-1:
        print(len(s)*k//2)
        sys.exit()

if k==1 or s[0]!=s[-1]:
    x = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            x += 1
            s[i+1] = 0
    print(x*k) 
    sys.exit()

if s[0]==s[-1]:
    b = 1
    x = 0
    while True:
        if s[x]==s[x+1]:
            b += 1
            x += 1
        else:
            break
    a = 1
    x = 0
    while True:
        if s[-1-x]==s[-2-x]:
            a += 1
            x += 1
        else:
            break
    x = 0
    for i in range(len(s)-1):
        if s[i]==s[0]:
            continue
        if s[i]==s[i+1]:
            x += 1
            s[i+1] = 0
    print(x*k+((a+b)//2)*(k-1)+a//2+b//2)

