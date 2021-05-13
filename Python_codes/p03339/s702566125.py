n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

s=list(input())

wtotal=s.count("W")
etotal=s.count("E")
wl=[];el=[]
wcount=0
ecount=0
for i in range(n):
    if s[i]=="E":
        ecount+=1
    el.append(ecount)
for i in range(n-1,-1,-1):
    if s[i]=="W":
        wcount+=1
    wl.append(wcount)

wl.reverse()
mn=etotal-el[0]
for i in range(n):
    mn=min(mn,wtotal-wl[i]+etotal-el[i])

print(mn)
