import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    if N == 0:
        if A[0] == 1: return 1
        else: return - 1
    elif A[0] != 0: return - 1
    mx = [0] * (N + 2)
    mx[0] = 1
    mx[N + 1] = 0
    mn = [0] * (N + 2)
    mn[0] = 1
    mn[N + 1] = 0
    n2 = 1
    for i in range(1, N + 1):
        n2 *= 2
        mx[i] = min(n2, (mx[i - 1] - A[i - 1]) * 2)
        mn[i] = mn[i - 1] - A[i - 1]
    for i in range(N, -1, -1):
        tmx = mx[i + 1] + A[i]
        tmn = A[i] + (mn[i + 1] + 1) // 2
        if tmx < 1 or tmx < mn[i]: return -1
        if tmn > mx[i]: return -1
        if tmx < tmn: return -1
        mx[i] = min(mx[i], tmx)
    return sum(mx)

if __name__ == '__main__':
    print(main())
