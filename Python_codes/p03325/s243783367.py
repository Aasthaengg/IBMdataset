n = int(input())
s = list(map(int,input().split()))

ans = 0
for i in s:
    while i%2 == 0:
        ans += 1
        i = i/2

print(ans)