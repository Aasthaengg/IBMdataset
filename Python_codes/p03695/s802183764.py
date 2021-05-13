N=int(input())
a=list(map(int,input().split()))
cnt=[0]*9
ans=0
for score in a:
    if score <400: 
        cnt[0]+=1
    elif score <800: 
        cnt[1]+=1
    elif score<1200:
        cnt[2]+=1
    elif score<1600:
        cnt[3]+=1
    elif score<2000:
        cnt[4]+=1
    elif score<2400:
        cnt[5]+=1
    elif score<2800:
        cnt[6]+=1
    elif score<3200:
        cnt[7]+=1
    else:
        cnt[8]+=1
for i in cnt[:8:]:
    if i:
        ans+=1
print(max(1,ans),ans+cnt[8])