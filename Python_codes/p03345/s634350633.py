def resolve():
    '''
    code here
    '''
    A, B, C, K = [int(item) for item in input().split()]

    if K % 2 == 0:
        res = A- B
    else:
        res = B -A

    print(res)
if __name__ == "__main__":
    resolve()
