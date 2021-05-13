n,t=map(int,input().strip().split(" "))
c=[]
time=[]
for i in range(n):
    a,b=map(int,input().strip().split(" "))
    if b<=t:
        c.append(a)
if c==[]:
    print("TLE")
else:
    print(min(c))