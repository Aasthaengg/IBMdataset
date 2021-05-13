N = int(input())
X = input()
X_arr = list(X)
N, X = int(N), int(X, 2)
MAX_N = 2 * 10 ** 5


def popcount(x):
    cnt = 0
    for i in range(x.bit_length()):
        if x & 1 << i:
            cnt += 1
    return cnt


memo = [0] * (MAX_N + 1)
for i, n in enumerate(range(1, MAX_N + 1), start=1):
    cnt = 0
    while n:
        p = popcount(n)
        n = n % p
        cnt += 1
    memo[i] = cnt


x_popcount = popcount(X)
p_upper, p_downer = x_popcount + 1, x_popcount - 1
y_upper = X % p_upper
y_downer = X % p_downer if p_downer else None

for i in range(N):
    if X_arr[i] == '0':
        z = (y_upper + pow(2, (N - i - 1), p_upper)) % p_upper
    else:
        if not p_downer:
            print(0)
            continue
        z = (y_downer - pow(2, (N - i - 1), p_downer)) % p_downer

    print(memo[z] + 1)
