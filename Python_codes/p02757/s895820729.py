
n, p = map(int, input().split())
s = list(map(int, list(input())))


cnt = [0] * p
cnt[0] = 1
rem = 0
sum = 0

if p == 2 or p == 5:
    for i in range(n):
        if s[i] % p == 0:
            sum += i + 1

else:
    for i in range(n):
        rem = (int(s[-i - 1]) * pow(10, i, p) + rem) % p
        sum += cnt[rem]
        cnt[rem] += 1

print(sum)