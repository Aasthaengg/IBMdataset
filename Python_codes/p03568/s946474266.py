def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 1
    for i in range(N):
        if A[i]%2==1:
            pass
        else:
            ans *= 2
        
    print(3**N-ans)
if __name__ == '__main__':
    main()