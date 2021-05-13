a = list(map(int,input().split()))
ans = [x for x in set(a) if a.count(x) < 2]
print(int(ans[0]))