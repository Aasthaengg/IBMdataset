def main():
    N = input()
    A = list(map(int, input().split()))

    cnt = 0
    for i in range(len(A)):
        if A[i]!=i+1:
            cnt+=1

    if cnt == 0 or cnt ==2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()