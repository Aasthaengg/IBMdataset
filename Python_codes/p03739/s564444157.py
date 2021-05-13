def solve(f, A):
    r, s = 0, 0
    for a in A:
        s += a
        if s == 0:
            r += 1
            s = f
        elif s * f < 0:
            r += -(s * f) + 1
            s = f
        f = -f
    return r

def main():
    N = int(input())
    A = list(map(int, input().split()))
    return min(solve(1, A), solve(-1, A))

print(main())
