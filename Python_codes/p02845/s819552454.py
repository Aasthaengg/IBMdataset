n = int(input())
a = list(map(int, input().split()))
current = [-1]*3
MOD = 1000000007
res = 1
for c in a:
    cnt = 0
    for can in current:
        if can == c-1:
            cnt += 1
    for i, v in enumerate(current):
        if v == c-1:
            current[i] = c
            break

    res *= cnt
    res %= MOD

res %= MOD
print(res)