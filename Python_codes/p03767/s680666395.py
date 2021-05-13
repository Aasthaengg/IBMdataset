n = int(input())
a_li = list(map(int,input().split()))
a_li.sort()
ans = 0
for i in range(1,n+1):
    ans += a_li[3*n-1-(i*2-1)]
print(ans)