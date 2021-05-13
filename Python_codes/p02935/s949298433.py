n=int(input())
li=list(map(int, input().split()))
li.sort()
ans=li[0]
for i in range(1,n):
    ans=(ans+li[i])/2
print(ans)