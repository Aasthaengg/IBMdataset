n = int(input())
ai = [int(input()) for i in range(n)]

tmp = ai[n-1]
ans = 0
ren = 0

if ai[0] != 0:
    print(-1)
    exit()

for i in range(1,n):
    if tmp - 1 > ai[n-i-1]:
        print(-1)
        exit()
    #print(i,n-i-1)
    if tmp - 1 == ai[n-i-1]:
        tmp -= 1
        ren += 1
        #print(ai[n-i-1],n-i-1)
    else:
        ans += ai[n-i]
        ans += ren
        #print(ans,ans,ans)
        tmp = ai[n-i-1]
        ren = 0

ans += ai[0]
ans += ren
    
print(ans)