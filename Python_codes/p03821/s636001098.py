N=int(input())
L=[list(map(int,input().split(' '))) for i in range(N)]
ans = 0
for a,b in L[::-1]:
    a+=ans
    ans += (b-a)%b
print(ans)