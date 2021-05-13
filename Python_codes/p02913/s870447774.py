import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 二分探索
N = ir()
S = sr()

def check(x):
    candidate = set()
    for i in range(N - 2*x + 1):
        candidate.add(S[i:i+x])
        if S[i+x:i+2*x] in candidate:
            return True
    return False

left = 0 # 可能
right = N
while right > left + 1:
    mid = (right+left) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
# 54