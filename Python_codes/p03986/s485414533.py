x=list(input())
num=[]
s="S"
cnt=len(x)
for i in range(len(x)):
    if x[i]==s:
        cnt=i
        break
cnt2=0
for i in range(cnt,len(x)):
    if x[i]!=s:
        if s=="T":
            s="S"
        else:
            s="T"
        num.append(cnt2)
        cnt2=1
    else:
        cnt2+=1
num.append(cnt2)
ans=0
num3=0
if len(num)%2==1:
    del(num[-1])
for i in range(len(num)//2):
    if num[-2*(i+1)]>=num[-2*i-1]+num3:
        ans+=(num[-2*i-1]+num3)*2
        num3=0
    else:
        ans+=(num[-2*(i+1)])*2
        num3=num[-2*i-1]+num3-num[-2*(i+1)]
print(len(x)-ans)
