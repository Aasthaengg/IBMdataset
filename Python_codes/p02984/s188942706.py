n = int(input())
a = list(map(int, input().split()))

s = sum(a)

ans = []
ans.append(s-2*sum(a[1::2]))
for i in range(n-1):
    ans.append(2*a[i] - ans[-1])
print(' '.join(list(map(str, ans))))