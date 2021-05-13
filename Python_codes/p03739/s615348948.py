N = int(input())
A = tuple(map(int,input().split()))

def solve(f):
    acc = 0
    cnt = 0
    for a in A:
        acc += a
        if f and acc <= 0:
            cnt += 1 - acc
            acc = 1
        elif not f and acc >= 0:
            cnt += acc + 1
            acc = -1
        f = not f
    return cnt

print(min(solve(True),solve(False)))