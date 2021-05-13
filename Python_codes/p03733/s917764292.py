n,t = map(int, input().split())
a = list(map(int, input().split()))
ans=0
last_start=0
for i in range(1,len(a)):
    if last_start + t > a[i]: # continuous
        ans += (a[i] - last_start)
    else: # stop -> start
        ans+=t
    last_start=a[i]
ans+=t

print(ans)