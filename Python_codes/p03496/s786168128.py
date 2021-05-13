n=int(input())
a=list(map(int,input().split()))
pos,zero,neg=0,0,0
maxi=-10**10
mini=10**10
for num in a:
    if num>0:
        pos+=1
    elif num==0:
        zero+=1
    else:
        neg+=1
    maxi=max(maxi,num)
    mini=min(mini,num)
maxidx=a.index(maxi)
minidx=a.index(mini)
if neg==0:
    print(n-1)
    for i in range(1,n):
        print(i,i+1)
elif pos==0:
    print(n-1)
    for i in reversed(range(1,n)):
        print(i+1,i)
else:
    print(2*n-2)
    if abs(maxi)>=abs(mini):
        for i in range(n):
            if i!=maxidx:
                print(maxidx+1,i+1)
        for i in range(1,n):
            print(i,i+1)
    else:
        for i in range(n):
            if i!=minidx:
                print(minidx+1,i+1)
        for i in reversed(range(1,n)):
            print(i+1,i)