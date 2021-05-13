n,k=map(int,input().split())
s=input()
s+="2"
lst=[]
ruiseki=[0]
i=0;cnt=1;ans=0
while True:
    if s[i]==s[i+1]:
        i+=1
        cnt+=1
    else:
        lst.append(cnt)
        ruiseki.append(ruiseki[-1]+cnt)
        i+=1
        cnt=1 
    if i==n:
        break
if s[0]=="1":
    flag=True
    if 2*k>=len(lst)-1:
        print(ruiseki[-1])
        exit()
else:
    flag=False
    if 2*k>=len(lst):
        print(ruiseki[-1])
        exit()

for i in range(1,len(lst)):
    if flag:
        ans=max(ans,ruiseki[min(i+2*k,len(lst))]-ruiseki[i-1])
        flag=False
    else:
        ans=max(ans,ruiseki[min(i+2*k-1,len(lst))]-ruiseki[i-1])
        flag=True
print(ans)