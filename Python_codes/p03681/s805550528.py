n, m = map(int, input().split())
if abs(n - m) >= 2:
    print(0)
else:
    dog = 1
    for i in range(1, n+1):
        dog = (dog * i) % (10 ** 9 + 7)
    monkey = 1
    for j in range(1, m+1):
        monkey = (monkey * j) % (10 ** 9 + 7)
    ans = dog * monkey
    if n == m:
        ans *= 2
    print(ans % (10 ** 9 + 7))
