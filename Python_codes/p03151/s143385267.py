n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if sum(a) < sum(b):
    print(-1)
    exit()

ans = 0
memo = []
tmp = 0

for i in range(n):
    if a[i] >= b[i]:
        memo.append(a[i]-b[i])
    else:
        tmp += b[i]-a[i]
        ans += 1

memo.sort(reverse = True)

if len(memo) != len(a):
    for j in memo:
        if j < tmp:
            tmp -= j
            ans += 1
        else:
            ans += 1
            break

print(ans)