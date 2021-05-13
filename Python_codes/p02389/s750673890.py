if __name__ == '__main__':
    a, b = [int(i) for i in input().split()]
    S, L = a*b, 2*(a+b)
    print(S, L)