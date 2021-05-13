a,b,t=map(int,input().split())

time=a
cnt=0
i=1
while time <= t+0.5:
    cnt+=b
    i +=1
    time += a

print(cnt)
