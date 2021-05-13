x,y = map(int,input().split())
nsum = x
ans = 1
while(nsum<=y):
    nsum=nsum*2
    if(nsum>y):
        break
    ans += 1
print(ans)