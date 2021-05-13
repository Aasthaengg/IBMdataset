s=input()
t=input()

ans1=0
ans2=0

ss=s*2

for i in range(len(t)):
    a=ss.find(t[i],ans2)
    if a==-1:
        ans=-1
        break
    if a>=len(s):
        ans1+=1
    ans2=a%(len(s))+1
    ans=ans1*len(s)+ans2
print(ans)