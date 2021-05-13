from fractions import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

def solve(N, M, A):
    while A[0] % 2 == 0:
        for idx, a in enumerate(A):
            if a % 2 != 0:
                return 0
            A[idx] //= 2
        M //= 2

    for a in A:
        if a % 2 == 0:
            return 0

    cur_lcm = 1
    for a in A:
        cur_lcm = lcm(cur_lcm, a)
        if M < cur_lcm:
            return 0
    return (M // cur_lcm + 1) // 2

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list((map(int, input().split())))
    A = [a // 2 for a in A]
    print(solve(N, M, A))