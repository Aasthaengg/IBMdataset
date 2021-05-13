n = int(input())
a = []
b = []
for i in range(n):
    a_e, b_e = map(int, input().split())
    a.append(a_e)
    b.append(b_e)

ans = 0

for i in range(n)[::-1]:
    mod = (a[i] + ans) % b[i]
    if mod != 0:
        ans += b[i] - mod

print(ans)