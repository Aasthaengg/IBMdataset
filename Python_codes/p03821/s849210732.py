n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    A, B = map(int, input().split())
    a[i], b[i] = A, B

a.reverse()
b.reverse()

ans = 0
for i in range(n):
    if (ans+a[i]) % b[i] == 0:
        cnt = 0
    else:
        cnt = b[i] - ((ans+a[i]) % b[i])
    ans += cnt
print(ans)