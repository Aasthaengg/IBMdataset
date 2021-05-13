def main():

    for i in range(1, K+1):
        for rm in cl:
            if rm > i:
                continue
            if dpt[i - rm] == 0:
                dpt[i] = 1
                break
        else:
            dpt[i] = 0

if __name__ == '__main__':
    N, K = map(int, input().split())
    cl = list(map(int, input().split()))
    dpt = [-1 for i in range(K+1)]
    dpt[0] = 0

    main()
    if dpt[K] == 0:
        print('Second')
    else:
        print('First')

