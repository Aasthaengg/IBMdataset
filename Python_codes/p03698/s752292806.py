def resolve():
    '''
    code here
    '''
    S = [item for item in input()]
    if len(S) == len(set(S)):
        print('yes')
    else:
        print('no')


if __name__ == "__main__":
    resolve()
