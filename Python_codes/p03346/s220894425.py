#backfront
N=int(input())
lists=[]
for _ in range(N):
    x=int(input())
    lists.append((_,x))
lists.sort(key=lambda x:x[1])
lists.append((-10000000000000000,"end"))

cnt=0
now=-1
maxi=0
for i in range(N+1):
    p=lists[i][0]
    if now<p:
        cnt+=1
        now=p
    elif now>p:
        maxi=max(maxi,cnt)
        cnt=1
        now=p
print(N-maxi)
