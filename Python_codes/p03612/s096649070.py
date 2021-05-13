n = int(input())
p = list(map(int, input().split()))

check = [0] * (n+10)
flag = 0
cnt = 0
for i in range(n):
    if flag == 0:
        if i+1 == p[i]:
            flag = 1
            cnt += 1
    else:
        if i+1 == p[i]:
            cnt += 1
        else:
            flag = 0
            check[cnt] += 1
            cnt = 0
else:
    check[cnt] += 1

ans = 0
for i in range(len(check)):
    s = i//2 + i%2
    ans += s*check[i]

print(ans)