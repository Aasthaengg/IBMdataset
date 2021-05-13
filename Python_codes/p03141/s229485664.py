n = int(input())
ab =[tuple(map(int, input().split( ))) for i in range(n)]
ab.sort(key = lambda x:x[0]+x[1],reverse = True)
ans = 0
for i in range(n):
    if i%2==0:
        ans += ab[i][0]
    else:
        ans -= ab[i][1]
print(ans)
