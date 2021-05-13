def f(x):
    return (sum(list(map(int, list(str(x))))))

ans = 0
n , a, b = map(int, input().split())
for i in range(1, n+1):
    if a <= f(i) <= b:
        ans += i
print(ans)