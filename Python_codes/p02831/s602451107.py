import math

def solve():
    ans = (A*B) // math.gcd(A,B)
    print(ans)

if __name__ == "__main__":
    A,B = list(map(int, input().split()))
    solve()