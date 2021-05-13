from itertools import permutations
N = int(input())
A = list(map(int, input().split()))

# 1 ^ 2 ^ 3 ^ 4 ^ 4 などが0になる順番は関係ない
# 各桁のビットが偶数になるかカウントする
D = [0] * 30
for a in A:
    bit = bin(a)[2:][::-1]
    for i in range(len(bit)):
        D[i] += int(bit[i])
# print('D', D)

ans = 'Yes' if all([d % 2 == 0 for d in D]) else 'No'
print(ans)
