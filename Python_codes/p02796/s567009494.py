from operator import itemgetter
n=int(input())
s=[""]*n
t=[""]*n
for i in range(n):
    x,l=map(int,input().split())
    s[i]=x-l
    t[i]=x+l
st=sorted([(s[i],t[i]) for i in range(n)], key=itemgetter(1))
ans=0
last=0
last=-float("inf")
for i in range(n):
    if last<=st[i][0]:
        ans+=1
        last=st[i][1]
print(ans)
