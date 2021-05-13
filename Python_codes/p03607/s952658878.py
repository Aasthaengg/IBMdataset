N = int(input())
S = set()
ans = 0
for i in range(N):
    a = int(input())
    if a in S:
        ans -= 1
        S.remove(a)
    else:
        ans += 1
        S.add(a)
print(ans)