n = int(input())
a = list(map(lambda x:int(x)-1, input().split()))

ans = 0
for i in range(n):
    if i == a[a[i]]: ans += 1
print(int(ans/2))