n,k,c=map(int,input().split())
#n日中k日働く。働いたらc日働かない

s=list(input())

#Xの時、i日後には働かない

ll=[]
rr=[]

day=0
while day<n:
    if s[day]=="o":
        ll.append(day)
        day+=(c+1)
    else:
        day+=1
    if len(ll)>=k:
        break

day=n-1
while 0<=day:
    if s[day]=="o":
        rr.append(day)
        day-=(c+1)
    else:
        day-=1
    if len(rr)>=k:
        break
        
rr=rr[::-1]
#print(ll)
#print(rr)

for i in range(k):
    if ll[i]==rr[i]:
        print(ll[i]+1)