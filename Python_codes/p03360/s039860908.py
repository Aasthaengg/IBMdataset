a,b,c=map(int,input().split())
k=int(input())
#print(a,b,c,k)

ans=0
for i1 in range(k+1):
    for i2 in range(k+1):
        for i3 in range(k+1):
#            print(i1,i2,i3)
            if (i1+i2+i3==k):
                temp=a*2**(i1)+b*2**(i2)+c*2**(i3)
#                print(temp)
                ans=max(ans,temp)

print(ans)

