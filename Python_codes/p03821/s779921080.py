n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
ans = 0
for i in range(n-1,-1,-1):
    x = (ab[i][1] - (ab[i][0]+ans)%ab[i][1])%ab[i][1]
    #print(x)
    ans += x

print(ans)

