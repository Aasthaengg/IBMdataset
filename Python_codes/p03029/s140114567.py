def solve():
    A, P = map(int, input().split())
    ans = (A*3+P)//2
    return ans
print(solve())