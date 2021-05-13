from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
a.sort()
a_acc = list(accumulate(a))[:-1]
ans = 1
for i in reversed(range(n-1)):
    if a_acc[i] * 2 >= a[i+1]:
        ans += 1
    else: break
print(ans)
