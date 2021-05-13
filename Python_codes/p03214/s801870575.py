N=int(input())
a = list(map(int, input().split()))
me=sum(a)/len(a)
mini=1000
ans=0
for i in range(N):
    if abs(a[i]-me)<mini:
        mini=abs(a[i]-me)
        ans=i
print(ans)