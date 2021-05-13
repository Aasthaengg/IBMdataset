def main(K, A, B):
    for i in range(A, B+1):
        if i%K==0:
            print('OK')
            return
    print('NG')
    return

if __name__ == '__main__':
    K = int(input())
    A, B = map(int, input().split())
    main(K, A, B)

