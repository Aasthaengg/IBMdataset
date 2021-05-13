k, a, b = map(int,input().split())
ans = 1

if b-a < 3 or a >= k:
    ans += k
else:
    ans += (a-1)
    k -= (a-1)
    tmp = k//2
    k -= 2*tmp
    ans += ((b-a)*tmp) + k%2

print(ans)
