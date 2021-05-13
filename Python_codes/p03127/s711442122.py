import math

def solve():
    ans = A[0]
    for i in range(1, N):  
        ans = math.gcd(ans, A[i])
    print(ans)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    solve()  
