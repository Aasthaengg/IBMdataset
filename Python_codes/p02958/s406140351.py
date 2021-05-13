n = int(input())
p = list(map(int, input().split()))
l = list(range(1,(n+1)))

if p == l:
    ans = "YES"
cnt = 0
for i in range(n):
    if p[i] != l[i]:
        if p[p[i]-1] == l[i]: cnt += 1
        else:
            ans = "NO"
            break
if cnt > 0:
    print("YES" if cnt//2 == 1 else "NO")
else:
    print(ans)