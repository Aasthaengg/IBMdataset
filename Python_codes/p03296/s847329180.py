n = int(input())
a = list(map(int, input().split()))

slime = []
cnt = 0
color = 0
for i in range(n):
    if i == 0:
        cnt = 1
        color = a[i]
        continue
    if a[i] == color:
        cnt += 1
    else:
        slime.append(cnt)
        cnt = 1
        color = a[i]
else:
    slime.append(cnt)

ans = 0
for i in slime:
    ans += i // 2
print(ans)
