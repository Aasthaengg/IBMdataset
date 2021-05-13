n = int(input())
a = list(int(input()) for i in range(n))
b = 1
ans = 0
while b != 2 and ans <= n:
    ans += 1
    b = a[b-1]
if ans > n:
    print(-1)
else:
    print(ans)