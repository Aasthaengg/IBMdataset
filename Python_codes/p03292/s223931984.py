a = sorted(list(map(int,input().split())))
ans = abs(a[1]-a[0])+abs(a[2]-a[1])
print(ans)