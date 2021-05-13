a,b=map(int,input().split())

heightl=[]
height=0
for i in range(1,1000):
    height+=i
    heightl.append(height)
#print(heightl)
for i in range(1000):
    cur=heightl[i]
    nex=heightl[i+1]
    if cur>a:
        if nex-b==cur-a:
            ans=cur-a
            break
print(ans)