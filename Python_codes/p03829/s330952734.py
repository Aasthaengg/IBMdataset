import sys
input = sys.stdin.readline

def main():
    N, A, B = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]

    ans = 0
    for i, j in zip(X, X[1:]):
        ans += min((j - i) * A, B)

    print(ans)

    
    
    

if __name__ == '__main__':
    main()



