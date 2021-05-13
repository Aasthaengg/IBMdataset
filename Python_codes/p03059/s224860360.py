a,b,t=map(int,input().split())
time=a
n=0
while time<t+0.5:
    n+=1
    time+=a
print(b*n)