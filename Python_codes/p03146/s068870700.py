def resolve():
    '''
    code here
    '''
    s = int(input())
    is_not_found = True
    cnt = 1
    memo = [False for _ in range(10**7+1)]

    while memo[s] == False:
        cnt += 1
        memo[s] = True
        if s % 2 == 0:
            s //= 2
        else:
            s = 3*s + 1    

    print(cnt)


if __name__ == "__main__":
    resolve()
