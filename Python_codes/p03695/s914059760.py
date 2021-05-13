n = int(input())
a = list(map(int, input().split()))

a.sort()

if a[0] >= 3200:
    print(1, n)
    exit()

ans = [0] * 9
for i in a:
    if i >= 3200:
        ans[8] += 1
    else:
        ans[i//400] = 1

print(sum(ans) - ans[-1], sum(ans))