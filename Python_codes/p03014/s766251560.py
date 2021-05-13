h,w=map(int,input().split())
lists=[]
for i in range(h):
    s=input()
    lists.append(s)
ylists=[]
for some in lists:
    some=some+"#"
    cnt=0
    add=[]
    for i in range(w+1):
        if some[i]=="#":
            if cnt==0:
                add.append(0)
                cnt=0
            else:
                add.extend([cnt]*cnt)
                add.append(0)
                cnt=0
                
        elif some[i]!="#":
            cnt+=1
    del add[-1]
    ylists.append(add)
    

            
lists1=[]
for i in range(w):
    adds=""
    for j in range(h):
        adds+=lists[j][i]
    lists1.append(adds)
    
tlists=[]
for some in lists1:
    some=some+"#"
    cnt=0
    add=[]
    for i in range(h+1):
        if some[i]=="#":
            if cnt==0:
                add.append(0)
                cnt=0
            else:
                add.extend([cnt]*cnt)
                add.append(0)
                cnt=0
                
        elif some[i]!="#":
            cnt+=1
    del add[-1]
    tlists.append(add)


maximum=0
for i in range(h):
    for j in range(w):
        if ylists[i][j]==0 or tlists[j][i]==0:
            continue
        else:
            maximum=max(maximum,ylists[i][j]+tlists[j][i]-1)
print(maximum)    
