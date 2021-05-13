def resolve():
    S = list(input())
    if len(S)%2 == 0:
        s1, s2 = S[:len(S)//2], S[len(S)//2:]
    else:
        s1, s2 = S[:len(S)//2], S[(len(S)//2)+1:]
    s2.reverse()
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    print(cnt)


if '__main__' == __name__:
    resolve()