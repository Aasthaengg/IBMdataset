n, x = map(int,input().split())
li = list(map(int,input().split()))

if sum(li) < x:
    print(n-1)
    exit()

li.sort()
ans = 0

for i in li:
    x -= i
    if x >= 0:
        ans += 1

print(ans)