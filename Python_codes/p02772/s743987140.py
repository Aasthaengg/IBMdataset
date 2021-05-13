def main():
    N, A = int(input()), list(map(int, input().split()))

    flag = True 

    for n in range(N):
        if A[n] % 2 == 0 and A[n] % 3 != 0 and A[n] % 5 != 0:
            flag = False
    
    print('APPROVED') if flag else print('DENIED') 


if __name__ == '__main__':
    main()

