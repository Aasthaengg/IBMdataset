abc = list(map(int,input().split()))
maxnum = max(abc)
parity = maxnum%2
ans = 0
for i in abc:
    if i%2==parity:
        ans+=(maxnum-i)//2+1
    else:
        ans+=(maxnum-1-i)//2
if abc[0]%2==abc[1]%2 and abc[1]%2==abc[2]%2:
    ans-=3
print(ans)