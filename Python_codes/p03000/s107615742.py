n,x = map(int,input().split())
li = list(map(int,input().split()))

ans = 1
D = 0
for i in li:
    D += i
    if D <= x:ans += 1
print(ans)