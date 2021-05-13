a=int(input())
b=int(input())
ans=1
cnt=0
while cnt<a:
    if ans>b:
        break
    ans=ans*2
    cnt+=1
if cnt<a:
    ans=ans+((a-cnt)*b)
print(ans)