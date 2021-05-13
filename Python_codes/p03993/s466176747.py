N = int(input())
a = list(map(lambda x:int(x)-1,input().split()))
ans = 0
for i in range(N):
    if a[a[i]] == i:
        ans += 1
print(ans//2)