N = int(input())

a = [int(input()) for _ in range(N)]

st = 0
ans = 0
a.sort()
for i in range(N):
    if a[i] == st:
        ans -= 1
        st = 0
    else:
        ans += 1
        st = a[i]
print(ans)