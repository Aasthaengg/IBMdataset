n = int(input())
A = []

for i in range(n):
    a = int(input())
    A.append(a)
A.sort()
i = 0
ans = 0
while True:
    cnt = 0
    while A[i + cnt] == A[i]:
        cnt += 1
        if i + cnt == n:
            break
    if cnt%2 == 1:
        ans += 1
    i += cnt
    if i == n:
        break
print(ans)