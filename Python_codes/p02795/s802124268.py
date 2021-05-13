h = int(input())
w = int(input())
n = int(input())
m = max(h, w)
ans = n // m
if n % m != 0:
    ans += 1
print(ans)