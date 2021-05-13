s=input()
cnt=[0]*3
for i in range(len(s)):
    if s[i]=="a":
        cnt[0]+=1
    elif s[i]=="b":
        cnt[1]+=1
    else:
        cnt[2]+=1
m=min(cnt)
for i in range(3):
    cnt[i]-=m
if max(cnt)<=1:
    print("YES")
else:
    print("NO")
