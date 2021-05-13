def main():
    S = input()
    if S[0] != 'k':
        return ('NO')
    elif S == 'keyence':
        return ('YES')

    ans = 'keyence'
    i = 0
    j = 0
    while True:
        i += 1
        j += 1
        if S[i] != ans[j]:
            break

    #残りの文字数
    num = 7-j
    cnt = 0
    while cnt < num:
        cnt += 1
        #print(ans[-cnt])
        if S[-cnt] != ans[-cnt]:
            return ('NO')
    return ('YES')
print(main())
