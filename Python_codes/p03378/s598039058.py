def resolve():
    '''
    code here
    '''
    N, M, X = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]

    low = [item for item in As if item < X]
    high = [item for item in As if item > X]

    print(min(len(low), len(high)))


if __name__ == "__main__":
    resolve()
