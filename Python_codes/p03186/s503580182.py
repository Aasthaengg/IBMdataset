def solve():
    A, B, C = map(int, input().split())
    print(B + min(C, A+B+1))

if __name__ == '__main__':
    solve()