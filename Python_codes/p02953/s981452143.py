n=int(input())
m=list(map(int,input().split()))
h=m[::-1]
for i in range(1,n):
    if h[i]>h[i-1]+1:
        print('No')
        exit()
    elif h[i]==h[i-1]+1:
        h[i]-=1
print('Yes')