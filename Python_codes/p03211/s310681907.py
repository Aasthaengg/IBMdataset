def resolve():
    '''
    code here
    '''
    S = input()
    res = 99999
    num = len(S)
    for i in range(num-1):
        res = min(res, abs(int(S[i:i+3]) - 753))

    print(res)
if __name__ == "__main__":
    resolve()
