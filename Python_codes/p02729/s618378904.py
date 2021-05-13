if __name__ == '__main__':

    n,m = map(int,input().split())

    eve = (n*(n-1)) // 2
    odd = (m*(m-1)) // 2
    print(eve+odd)
