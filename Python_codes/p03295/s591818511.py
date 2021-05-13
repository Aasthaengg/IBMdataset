import sys
input=sys.stdin.readline
n,m=map(int,input().split())
war=[]
for i in range(m):
    start,end=map(int,input().split())
    war.append([start,end])
war=sorted(war,key=lambda x:x[1])
end=0
ans=0
for i in war:
    if i[0]>=end:
        ans+=1
        end=i[1]
print(ans)