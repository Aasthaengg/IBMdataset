n,m=map(int,input().split())
lists=[0 for i in range(m)]
for i in range(m):
    x,y=map(int,input().split())
    lists[i]=(x,y)
anslist=[0 for i in range(n+1)]
#anslist[1] からanslist[n]まででこれらが全て偶数となるような時を考えればいい
#そうでないならばそれはNoである
for j in lists:
    if j[0]==1:
        anslist[j[1]]+=1
        
    elif j[1]==1:
        anslist[j[0]]+=1
        
    else:
        x=j[0]
        y=j[1]
        anslist[x]+=1
        anslist[y]+=1
flag=True
for k in anslist:
    if k%2!=0:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")