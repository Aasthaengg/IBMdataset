N = int(input())
A = list(map(int, input().split(' ')))
mod = 10 ** 9 + 7
c = [0, 0, 0]
ans = 1
for i in A:
    ans *= c.count(i)
    if i == c[0]:
        c[0] += 1
    elif i == c[1]:
        c[1] += 1
    else:
        c[2] += 1
    ans %= mod
print(ans)
