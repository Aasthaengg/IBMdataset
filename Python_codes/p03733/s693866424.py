n, t = map(int, input().split())
ts = list(map(int, input().split()))
ans = 0

for num, s in enumerate(ts):
    try:
        if ts[num] + t <= ts[num+1]:
            ans += t
        else:
            ans += ts[num+1] - ts[num]
    except:
        pass
ans += t
print(ans)
