n = int(input())
a = list(map(int, input().split()))
a.sort()
rui = [a[0]]
for i in range(1, n):
    rui.append(rui[i-1] + a[i])
col = [1 for i in range(n)]
for i in range(n-1):
    if 2*rui[i] < a[i+1]:
        col[i] = 0
ans = 0
for i in range(n-1, -1, -1):
    if col[i] == 1:
        ans += 1
    else:
        break
print(ans)