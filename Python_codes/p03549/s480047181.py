n,m=map(int,input().split())

ac=(n-m)*100
tle=m*1900
time=0
cnt=1
time_ac=(ac+tle)*(1/2)**m
fault=(1-(1/2)**m)
while True:
    temp=cnt*time_ac*(fault**(cnt-1))
    if time==time+temp:
        print(round(time))
        break
    time+=temp
    cnt+=1
