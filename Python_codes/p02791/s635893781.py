n = int(input())
p = list(map(int,input().split()))
curmin = 2*10**5+1
ans = 0

for i in p:
    if curmin >= i:
        curmin = min(curmin, i)
        ans += 1

print(ans)