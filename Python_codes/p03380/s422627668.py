import bisect
def main():
    N = int(input())
    A = sorted([int(_) for _ in input().split()])
    r = A[-1]//2
    B = A[:-1]
    x = bisect.bisect_left(B, r)
    if x == 0:
        return A[-1], B[x]
    elif x == N-1:
        return A[-1], B[x-1]
    else:
        if abs(B[x]-r) <= abs(B[x-1]-r): return A[-1], B[x]
        else: return A[-1], B[x-1]
if __name__ == '__main__':
    print(*main())
