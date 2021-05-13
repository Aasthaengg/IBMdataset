a,b = map(int,input().split())
a -= 1
b -= 1
ans = b//a
if b%a != 0:
    ans += 1
print(ans)
