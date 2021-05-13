n = int(input())

if n == 2:
    print(1)
    exit()

ans = set()
for i in range(2, int((n-1) ** 0.5) + 1):
    if (n-1) % i == 0:
        ans.add(i)
        ans.add((n-1) // i)

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        k = i
        temp = n
        while temp % k == 0:
            temp //= k
        if temp % k == 1:
            ans.add(k)
        k = n // i
        temp = n
        while temp % k == 0:
            temp //= k
        if temp % k == 1:
            ans.add(k)

print(len(ans) + 2)