n=int(input())
t=1
while n>t:
    n-=t
    t+=1
rem=t-n
las=t
for i in range(1,las+1):
    if i!=rem:
        print(i)