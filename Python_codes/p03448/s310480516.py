import itertools

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    a = [x for x in range(A+1)]
    b = [x for x in range(B+1)]
    c = [x for x in range(C+1)]
    ans = 0
    for i,j,k in itertools.product(a,b,c):
        if X == 500*i + 100*j + 50*k:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()