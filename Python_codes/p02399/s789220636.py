if __name__ == '__main__':
    a, b = [int(i) for i in input().split()]
    d, r, f = a//b, a%b, a/b
    print("{0} {1} {2:.6f}".format(d, r, f))