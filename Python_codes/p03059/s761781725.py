a,b,t=map(int,input().split())
time=0
bis=0
while (time+a<=t+0.5):
    bis+=b
    time+=a
print(bis)