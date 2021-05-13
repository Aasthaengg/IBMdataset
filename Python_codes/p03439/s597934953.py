def main():
    n = int(input())

    def q(i):
        print(i, )
        s = str(input())
        if s == 'Vacant':
            exit()
        else:
            return s

    x = q(n-1)
    x = q(0)

    def ok(m):
        if m == 0:
            return False
        else:
            if (m%2 == 0 and q(m) != x) or (m%2 == 1 and q(m) == x):
                return True
            else:
                return False

    l = 0
    r = n-1
    while l+1 < r:
        c = (l+r)//2
        if ok(c):
            r = c
        else:
            l = c

if __name__ == '__main__':
    main()