n = int(input())
a = [int(input()) for _ in range(n)]
s = set()
i, ans = 1, 0

while i != 2:
    if i in s:
        ans = -1
        break
    else:
        s.add(i)
        i, ans = a[i-1], ans+1
print(ans)