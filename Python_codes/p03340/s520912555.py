n = int(input())
a = list(map(int, input().split()))

bit_len = 20
memo = [[] for i in range(bit_len)]
ans = 0

for i, ai in enumerate(a):
    li = 0
    for j in range(bit_len):
        if ai & (1 << j):
            if len(memo[j]) >= 1:
                li = max(li, memo[j][-1] + 1)
            memo[j].append(i)
        else:
            if len(memo[j]) >= 2:
                li = max(li, memo[j][-2] + 1)
    ans += i - li + 1

print(ans)
