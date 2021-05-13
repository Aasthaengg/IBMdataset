a = sorted(list(map(int,input().split())))
ans = int(str(a[-1])+str(a[-2])) + a[0]
print(ans)
