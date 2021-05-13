import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    C = [int(c) for c in input().split()]
    C.append(10 ** 10)
    A.sort()
    B.sort()
    C.sort()
    B_choise = [0] * N
    C_i = 0
    for i, b in enumerate(B):
        while C[C_i] <= b: C_i += 1
        B_choise[i] = N - C_i
    B_choise_sum = [0] * (N + 1)
    for i in reversed(range(N)):
        B_choise_sum[i] = B_choise_sum[i+1] + B_choise[i]
    
    B.append(10 ** 10)
    B_i = 0
    Ans = 0
    for i, a in enumerate(A):
        while B[B_i] <= a: B_i += 1
        Ans += B_choise_sum[B_i]
    print(Ans)
  
    return 0

if __name__ == "__main__":
    solve()