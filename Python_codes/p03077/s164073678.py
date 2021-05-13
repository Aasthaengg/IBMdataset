n = int(input())
L = [int(input()) for _ in range(5)]

ans = 5
if n%min(L) == 0:
    ans += n//min(L)-1
else:
    ans += n//min(L)+1-1
print(ans)
