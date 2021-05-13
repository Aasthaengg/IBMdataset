N=int(input())
li=list(map(int,input().split()))
ans=0
li.sort()

H=int(N//2)

for i in range(1,10**5+1):
    if li[H-1]<i and li[H]>=i:
        ans+=1

print(ans)
