a,b=map(int,input().split())

s=a+b
ss=s//2
s2=s%2

if s2==1:
    print(ss+1)
    exit()
print(ss)
