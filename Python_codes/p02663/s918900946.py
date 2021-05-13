from datetime import*
a,b,c,d,k=map(int,input().split())
f=datetime
print((f(1,1,1,c,d)-f(1,1,1,a,b)).seconds//60-k)