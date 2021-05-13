n=int(input())
ss=[]
tt=[]
for i in range(n):
    s,t=input().split()
    t=int(t)
    ss+=[s]
    tt+=[t]
x=input()
p=ss.index(x)
print(sum(tt)-sum(tt[:p+1]))