from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))
dic = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
usable = defaultdict(int)

for num in A:
    use = dic[num]
    if usable[use] < num:
        usable[use] = num

DP = [-1]*(n+10)
DP[0] = 0

for i in range(n):
    digits = DP[i]
    if digits < 0:
        continue

    for use in usable.keys():
        if i+use <= n and DP[i+use] < digits + 1:
            DP[i+use] = digits + 1
        else:
            continue

digits = DP[n]
num_of_match = n
ans = ''

for _ in range(n):
    if digits == 0:
        break

    for num in sorted(usable.values(), reverse=True):
        use = dic[num]
        if DP[num_of_match - use] == digits - 1:
            digits -= 1
            num_of_match -= use
            ans += str(num)
            break
        else:
            continue

print(ans)