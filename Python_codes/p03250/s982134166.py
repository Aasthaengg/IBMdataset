a = list(map(int,input().split()))
a = sorted(a,reverse = True)
ans = a[0] * 10 + sum(a[1:])
print(ans)

