n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
mx = 0
ans = 1
for i in range(1, n+1):
    v = i
    count = 0
    while v//2 != 0 and v % 2 == 0:
        count += 1
        v = v//2
    if count >= mx:
        ans = i
    mx = max(mx, count)
print(ans)
