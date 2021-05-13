n=int(input())
a=list(map(int,input().split()))

ans = 0
for i in range(n):

    if a[i] > i+1 and i+1 == a[a[i]-1]:

        ans+=1

    i+=1

print(ans)