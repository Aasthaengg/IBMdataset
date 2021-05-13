n = input()
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = a[0]

mid = int(len(a) / 2)
for i in range(1, mid):
    ans = ans + a[i] * 2
if len(a) % 2 == 1:
    ans = ans + a[mid]

print(ans)
