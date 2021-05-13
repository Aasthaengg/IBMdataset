k, a, b = list(map(int, input().split()))

ans = 1
if b >= a+3:
    if k >= a+1:
        ans += b-1

        ans += (b-a)*((k-(a+1))//2)
        ans += (k-(a+1)) % 2
    else:
        ans += k
else:
    ans += k

print(ans)