a = sorted(list(map(int,input().split())))
ans = 0
ans += abs(a[1]-a[2])
ans += abs(a[0]-a[1])
print(ans)
