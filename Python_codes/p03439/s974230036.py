import sys
n = int(input())

def _input():
    s = input()
    if s == 'Vacant':
        sys.exit(0)
    return s

# 偶数奇数一致判定
def check(x, y):
    # 性別一致の場合
    if x[1] == y[1]:
        if x[0] % 2 == y[0] % 2:
            return True
        else:
            return False
    else:
        if x[0] % 2 == y[0] % 2:
            return False
        else:
            return True

print(0, flush=True)
s = _input()
left = (0, s)

print(n-1, flush=True)
s = _input()
right = (n-1, s)

print(n//2, flush=True)
s = _input()
center = (n//2, s)

while(True):
    if check(left, center):
        left = center
        new_i = (center[0] + right[0]) // 2
        print(new_i, flush=True)
        center = (new_i, _input())
    else:
        right = center
        new_i = (left[0] + center[0]) // 2
        print(new_i, flush=True)
        center = (new_i, _input())