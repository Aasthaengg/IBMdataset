import sys
input = sys.stdin.readline


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]

# Cについて大きい順にソート
BC.sort(key=lambda x: x[1], reverse=True)

tmp = []
# tmpがN個を超えるまで、cをb個足す
for b, c in BC:
    tmp += [c] * b
    if len(tmp) >= N:
        break

# Aとtmpを混ぜてソート
nums = A + tmp
nums.sort(reverse=True)
# 上からN個の総和
print(sum(nums[:N]))
