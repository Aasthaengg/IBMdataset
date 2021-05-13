import sys
readline = sys.stdin.readline

def main():
    X, Y, Z, K = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    B = list(map(int, readline().rstrip().split()))
    C = list(map(int, readline().rstrip().split()))
    
    ab = [A[i] + B[j] for i in range(len(A)) for j in range(len(B))]
    ab = sorted(ab, reverse=True)[:K]

    abc = [ab[i] + C[j] for i in range(len(ab)) for j in range(len(C))]
    print(*sorted(abc, reverse=True)[:K], sep='\n')


if __name__ == '__main__':
    main()