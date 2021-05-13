n = int(input())
li = [int(x) for x in input().split()]
a = 10**6
ans = 0
for i in range(n-1):
    if li[i]==li[i+1]:
        li[i+1] = a
        a += 1
        ans += 1
print(ans)