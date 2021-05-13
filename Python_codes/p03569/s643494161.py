s=input()
exc_x=""
cnt=[]
now=0
for i in s:
    if i=="x":
        now+=1
    else:
        cnt.append(now)
        now=0
        exc_x+=i
cnt.append(now)
if exc_x!=exc_x[::-1]:
    print(-1)
    exit()
ans=0
n=len(cnt)
for i in range(n//2):
    ans+=abs(cnt[i]-cnt[n-i-1])
print(ans)