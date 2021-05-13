l=list(map(int,input().strip().split()))

l.sort()
x=l[2]-l[1]+(l[1]-l[0])//2
ans=x if (l[1]-l[0])%2==0 else x+2
print(ans) 