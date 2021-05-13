s,c = map(int,input().split())

a = c //2
if s >= a:
    ans = a
else:
    b = c - 2 * s
    ans = s + b//4
print(ans)