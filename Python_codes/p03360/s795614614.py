if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    n = int(input())
    a.sort()
    a[2] = a[2]*(2**n)
    print(sum(a))