def solve(N, A, B):
    if A % 2 == B % 2:
        return (B - A) // 2
    return min(A-1, N-B) + 1 + (B - A -1)//2

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    print(solve(n, a, b))
