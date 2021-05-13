import math

def solve(x, k, d):
    x = math.fabs(x)
    if x - k * d >= 0:
        return int(x - k * d)
    else:
        cur = x - x // d * d
        k = k - x // d
        if k % 2 == 0:
            return int(cur)
        else:
            return int(abs(cur - d))

if __name__ == "__main__":
    x, k, d = map(int, input().split(' '))
    print(solve(x, k, d))
