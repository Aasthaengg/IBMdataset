if __name__=="__main__":
    n, k = input().split(' ')
    n = int(n)
    k = int(k)
    if k * 2 - 1 <= n:
        print('YES')
    else:
        print('NO')