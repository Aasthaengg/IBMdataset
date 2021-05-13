n=int(input())
l=list(map(int,input().split()))
# print(l)
ans=1
if 0 in l:
    print(0)
    exit()
for i in l:
    ans*=i
    if ans> 10**18:
        # print(ans)
        print(-1)
        exit()
print(ans)