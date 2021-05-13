r=input().split()
A=int(r[0])
B=int(r[1])
x=1
n=0
while x<B:
    x+=A-1
    n+=1
print(n)