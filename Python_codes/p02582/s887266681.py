n=input()

ans=0
cnt=0
for str in n:
    if str=="R":
        cnt+=1
        ans=max(ans,cnt)
    else:
        cnt=0
print(ans)
