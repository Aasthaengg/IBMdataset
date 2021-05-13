s=input()
t=""
num=[]
for i in range(len(s)):
    if s[i]!="x":
        t+=s[i]
        num.append(i)
yn=0
for i in range(-(len(t)//-2)):
    if t[i]!=t[-1-i]:
        yn=1
        break
if yn==1:
    print(-1)
else:
    if len(num)==0:
        print(0)
    else:
        ans=abs(num[0]-(len(s)-num[-1]-1))
        for i in range(len(num)//2):
            ans+=abs((num[i+1]-num[i])-(num[-1-i]-num[-2-i]))
        print(ans)
