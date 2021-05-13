N = int(input())
a = list(map(int,input().split()))
if a.count(1) == 0:
    print(-1)
    exit()
i = 1
ans = 0
for j in a:
    if i == j:
        i += 1
    else:
        ans += 1
print(ans)