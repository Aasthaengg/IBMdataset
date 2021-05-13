n = int(input())
d,x = map(int,input().split())
ans = 0

for i in range(n):
    day = 1
    count = 0
    m = int(input())
    while d >= day:
        day += m
        count += 1
    ans += count
    
print(ans + x)

