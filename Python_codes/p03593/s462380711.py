H, W = map(int, input().split())
A = ""
inf = 1e5
cnt = {}
ans = "Yes"
for i in range(H):
    a = input()
    A += a

for a in A:
    if a not in cnt.keys():
        cnt[a] = 1
    else:
        cnt[a] += 1
jud = [inf, 0, 0, 0]
if H % 2 == 1 and W % 2 == 1:
    jud[2] = H//2+W//2
    jud[1] = 1
elif H % 2 == 1:
    jud[2] = W//2
elif W % 2 == 1:
    jud[2] = H//2
for i in cnt.values():
    b = i % 4
    jud[b] -= 1
    if jud[b] < 0:
        ans = "No"
print(ans)
