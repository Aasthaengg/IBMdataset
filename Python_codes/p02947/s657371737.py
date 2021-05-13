n = int(input())
A = []
for i in range(n):
    i = list(map(str,input()))
    i.sort()
    A.append(i)

A.sort()
tmp = A[0]
cnt = 0
ans = 0
for i in range(1,n):
    if tmp == A[i]:
        cnt += 1
    else:
        tmp = A[i]
        for j in range(cnt):
            ans += cnt
            cnt -= 1
if cnt >= 1:
    for j in range(cnt):
        ans += cnt
        cnt -= 1

print(ans)