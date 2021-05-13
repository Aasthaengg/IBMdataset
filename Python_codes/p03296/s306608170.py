n = int(input())
ans = 0
l = list(map(int,input().split()))
for i in range(1,n):
    if l[i] == l[i-1]:
        ans += 1
        l[i] = 1000000
print(ans)