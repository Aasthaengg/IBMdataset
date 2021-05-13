n = int(input())
n2 = n//2
d = sorted(list(map(int,input().split())))

max_n = max(d[:n2])
min_n = min(d[n2:])

ans = 0
for i in range(max_n+1,min_n+1):
    ans += 1

print(ans)