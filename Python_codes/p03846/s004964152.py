N = int(input())
a = list(map(int, input().split()))
a_comb = []
mod = 10 ** 9 + 7

for i in range(N):
    a_comb.append(abs(i - (N - 1 - i)))

if sorted(a_comb) == sorted(a):
    print(2 ** (N // 2) % mod)
else:
    print(0)