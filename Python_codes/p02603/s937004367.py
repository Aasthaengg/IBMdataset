import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = 1000
    k = 0

    for i in range(N-1):
        if A[i+1] - A[i] <= 0:
            continue
        
        k += m // A[i]
        m -= k * A[i]
        m += k * A[i+1]
        k = 0

    print(m)

main()