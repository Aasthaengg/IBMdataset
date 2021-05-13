import math

mod = 1000000007

def solve():
    N = int(input())
    ans = math.factorial(N) % mod
    print(ans)

if __name__ == "__main__":
    solve()
