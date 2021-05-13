N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
cnts = [0] * (N + 1)
cnts[0] = 3
ans = 1
for a in A:
    ans *= cnts[a]
    cnts[a] -= 1
    cnts[a+1] += 1
print(ans % mod)