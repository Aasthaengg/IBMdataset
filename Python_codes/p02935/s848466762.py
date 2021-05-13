def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    As.sort()

    res = As[0]
    for i in As[1:]:
        res = (res + i)/2
    print(res)
if __name__ == "__main__":
    resolve()
