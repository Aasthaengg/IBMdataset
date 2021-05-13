# solution

data = int(input())

data1 = [input(), input()]

mod = 10**9+7

i = 1 + (data1[0][0] != data1[1][0])

ans = 3 * i

while i < data:
    p = data1[0][i-1] == data1[1][i-1]
    if data1[0][i] == data1[1][i]:
        ans *= 1 + p
        i += 1
    else:
        ans *= 3 - p
        i += 2
    ans %= mod

print(ans)