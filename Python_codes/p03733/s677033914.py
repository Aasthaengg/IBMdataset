n, t = [int(w) for w in input().split()]
lt = [int(w) for w in input().split()]

s_on = lt[0]
end = s_on+t
ans = t
for _t in lt[1:]:
    if _t <= end:
        ans += _t+t-end
    else:
        ans += t
    end = _t+t

print(ans)
