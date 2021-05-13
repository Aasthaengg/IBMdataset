n = int(input())
l = list(map(int,input().split()))

sw='n'
ans=0
for i in range(1,n):
    if sw=='u':
        if l[i-1]-l[i]<=0:
            continue
        else:
            ans+=1
            sw='n'
    elif sw=='d':
        if l[i-1]-l[i]>=0:
            continue
        else:
            ans+=1
            sw='n'
    else:
        if l[i-1]-l[i]<0:
            sw='u'
        elif l[i-1]-l[i]>0:
            sw='d'
        else:
            continue

print(ans+1)