n, l = map(int, input().split())
taste = [l+i for i in range(n)]
ans = [abs(i) for i in taste]

del taste[ans.index(min(ans))]
print(sum(taste))
