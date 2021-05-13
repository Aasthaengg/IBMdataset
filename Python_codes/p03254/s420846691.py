def LI():
    return list(map(int, input().split()))


N, total = LI()
a = LI()
Nlist = [0]*N
a.sort()
ans = 0
if sum(a) == total:
    ans = N
elif sum(a) < total:
    ans = N-1
else:
    for i in range(N):
        if total == a[i]:
            ans += 1
            break
        elif total > a[i]:
            ans += 1
            total -= a[i]
        else:
            break
print(ans)
