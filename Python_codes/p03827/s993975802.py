def resolve():
    '''
    code here
    '''
    N = int(input())
    S = input()

    res = 0
    ans = 0
    for item in S:
        if item == 'I':
            res += 1
        else:
            res -= 1

        
        ans = max(ans, res)

    print(ans)


if __name__ == "__main__":
    resolve()
