n = int(input())
xxx = list(map(int, input().split()))
sort_xxx = sorted(xxx)
median = sort_xxx[n // 2 - 1]
for i in range(n):
    if xxx[i] <= median:
        ans = sort_xxx[n // 2]
    else:
        ans = sort_xxx[n // 2 - 1]
    print(ans)