n=int(input())
li=list(map(int,input().split()))
if 0 in li:
    print(0)
    exit()
ans=1

for i in li:
    ans=ans*i
    if ans>10**18:
        print(-1)
        exit()
print(ans)