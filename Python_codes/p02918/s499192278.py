n,k=map(int,input().split())
s=input()

cnt=0
lst=[]
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        cnt+=1
    else:
        lst.append(cnt)
        cnt=0

lst.append(cnt)

ans=n-sum(lst)-1

lst2=[]
for i in lst:
    for j in range(i//2):
        lst2.append(2)
    
    if i%2==1:
        lst2.append(1)

lst3=[]
xxxxx=lst2.count(1)

if xxxxx%2==1:
    lst3.append(1)

for i in range(xxxxx//2):
    lst3.append(2)

for i in range(lst2.count(2)):
    lst3.append(2)

lst3.sort()
lst3.reverse()

if len(lst3)>k:
    ans+=sum(lst3[:k])
else:
    ans+=sum(lst3)


print(ans)