n = int(input())
a = list(map(int, input().split()))
b = a[::-1]

if n == 0 and a[0] == 1:
    print(1)
    exit()

if a[0] >= 1:
    print(-1)
    exit()
    
ans = [0] * (n + 1)
for i in range(n):
    ans[i + 1] = ans[i] + b[i]

ans = ans[::-1]

ans = ans[1::]
a = a[1::]

res = 1
prev_cnt = 1

for i in range(n):
    cnt = min(prev_cnt * 2, ans[i] + a[i])
    if cnt < a[i]:
        print(-1)
        exit()
    res += cnt
    prev_cnt = cnt - a[i]
print(res)
