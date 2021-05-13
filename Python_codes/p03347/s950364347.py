n=int(input())
a=[int(input()) for i in range(n)]
if a[0]!=0:
    print(-1)
    exit()

ans=0
for i in range(n)[::-1]:
    if a[i]-a[i-1]>1:
        print(-1)
        exit()
    elif a[i]<=a[i-1]:
        ans+=a[i]
    else:
        ans+=1
print(ans)


