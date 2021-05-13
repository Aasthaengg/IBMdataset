n = int(input())
l = list(map(int,input().split()))
ans = 0
for i1, i2 in enumerate(l):
    for j in l[i1+1:]:
        ans += i2 * j
print(ans)