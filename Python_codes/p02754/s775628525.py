if __name__ == '__main__':

    n,a,b = map(int,input().split())

    tmp1 = (n // (a + b)) * a
    if tmp1 == 0:
        tmp2 = min(n,a)
    else:
        tmp2 = n % (a + b)
        tmp2 = min(a,tmp2)
    print(tmp1+tmp2)