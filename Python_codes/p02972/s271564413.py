n = int(input())
a = list(map(int, input().split()))
ans = [0] * n

def cnt_rem(ans, x):
    i = 2
    ret = 0
    while (x + 1) * i <= n:
        ret += ans[(x + 1) * i - 1]
        i += 1
    
    return ret % 2

for i in range(n - 1, -1, -1):
    cnt = cnt_rem(ans, i)
    if cnt != a[i]:
        ans[i] += 1

print(sum(ans))
for i in range(n):
    if ans[i] == 1:
        print(i + 1, end = " ")