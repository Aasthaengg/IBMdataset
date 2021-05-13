q = int(input())
prime = [True for _ in range(10 ** 5 + 1)]
prime[0] = False
prime[1] = False
ans = [0 for _ in range(10 ** 5 + 1)]
total = 0
for num in range(2, 10 ** 5 + 1):
    if prime[num]:
        tmp = num * 2
        while tmp <= 10 ** 5:
            prime[tmp] = False
            tmp += num
        if prime[(num + 1) // 2]:
            total += 1
    ans[num] = total
for _ in range(q):
    l, r = map(int, input().split())
    print(ans[r] - ans[l - 1])