n = int(input())
ans = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        j = n // i
        # print(i, j)
        if j < i-1:
            ans += i-i
            # print("p", i-1)
        if i < j-1:
            ans += j-1
            # print("p", j-1)

print(ans)