k, a, b = map(int, input().split())

if 2 < (b-a):
    if k-(a-1) >= 2:
        q, r = divmod(k-(a-1), 2)
        ans = (b-a)*q+r+a
    else:
        ans = k+1

else:
    ans = k+1

print(ans)
