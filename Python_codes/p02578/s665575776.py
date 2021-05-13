n = int(input())
A = [int(x) for x in input().split()]
maxv = 0
ans = 0
for a in A:
    if maxv > a:
        ans += maxv - a
    else:
        maxv = a
print(ans)