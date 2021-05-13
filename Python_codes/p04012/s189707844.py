def resolve():
    '''
    code here
    '''
    import collections
    w = input()
    cnt = collections.Counter(w)

    for i, v in cnt.items():
        if v %2 != 0:
            print('No')
            break
    else:
        print('Yes')

if __name__ == "__main__":
    resolve()
