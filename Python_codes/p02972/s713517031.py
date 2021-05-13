n = int(input())
a = [0] + list(map(int, input().split()))
ans = []
for i in range(n, 0, -1):
    j = 2 * i
    while j <= n:
        a[i] ^= a[j]
        j += i
    if a[i] == 1:
        ans.append(i)
print(len(ans))
if ans:
    print(' '.join(list(map(str, ans))))