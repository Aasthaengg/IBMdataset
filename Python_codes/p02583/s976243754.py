def resolve():
    from itertools import combinations
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    if n < 3:
        print(0)
        return

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i >= j or j >= k or i >= k:
                    continue
                if l[i] == l[j] or l[j] == l[k] or l[k] == l[i]:
                    continue
                if l[i] >= l[j] + l[k] or l[j] >= l[i] + l[k] or l[k] >= l[i] + l[j]:
                    continue
                ans += 1

    print(ans)

resolve()