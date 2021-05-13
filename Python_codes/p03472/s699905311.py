import math
def main():
    N, H = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    r = 0
    c = 0
    while r < N and A[0] < B[r]:
        c += B[r]
        r += 1
        if c >= H:
            return r
    return int(r + math.ceil((H-c)/A[0]))
print(main())
