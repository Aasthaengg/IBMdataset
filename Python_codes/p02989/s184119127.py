def resolve():
    '''
    code here
    '''
    N = int(input())
    Ds = [int(item) for item in input().split()]

    Ds.sort()

    print(Ds[N//2] - Ds[N//2 -1])


if __name__ == "__main__":
    resolve()
