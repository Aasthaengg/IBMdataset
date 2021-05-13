def main():
    n = int(input())
    A = list(map(int, input().split()))

    res = 1
    inc = 0
    dec = 0

    for i in range(n - 1):
        if A[i] < A[i+1]:
            inc += 1
        elif A[i] > A[i+1]:
            dec += 1
        
        if inc and dec:
            res += 1
            inc, dec = 0, 0
    
    print(res)

if __name__ == '__main__':
    main()