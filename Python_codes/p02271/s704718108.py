def ALDS1_5A():
    n, A, q = int(input()),list(map(int, input().split())), int(input())
    allFromA = [False]*2001
    for a in A:
        for i in range(2000-a, 0, -1):
            if allFromA[i]:
                allFromA[i+a] = True
        allFromA[a] = True

    for m in input().split():
        if allFromA[int(m)]:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    ALDS1_5A()