N = int(input())
A = map(int, input().split())
ans = 0
pre = -1
for a in A:
    if a == pre:
        ans += 1
        pre = -1
    else:
        pre = a
print(ans)