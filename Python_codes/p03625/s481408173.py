n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
x=1
l=[]
for i in range(n-1):
    if i!=n-2:
        if a[i]==a[i+1]:
            x+=1
        else:
            if x>=4:
                l.append(a[i])
                l.append(a[i])
                break
            elif x==2 or x==3:
                l.append(a[i])
                x=1
                if len(l)>=2:
                    break
    else:
        if a[i]==a[i+1]:
            x+=1
            if x>=4:
                l.append(a[i])
                l.append(a[i])
                break
            elif x==2 or x==3:
                l.append(a[i])
                x=1
                if len(l)>=2:
                    break
        else:
            if x>=4:
                l.append(a[i])
                l.append(a[i])
                break
            elif x==2 or x==3:
                l.append(a[i])
                x=1
                if len(l)>=2:
                    break
#print(a,x)
if len(l)<2:
    print(0)
else:
    print(l[0]*l[1])