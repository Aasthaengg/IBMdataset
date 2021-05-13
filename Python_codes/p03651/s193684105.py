def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    N, K = map(int, input().split())
    A = tuple(map(int, input().split()))
    MAX_VAL = max(A)

    A_GCD = A[0]

    for a in A:
        A_GCD = gcd(A_GCD, a)
    
    if K <= MAX_VAL and K % A_GCD == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()