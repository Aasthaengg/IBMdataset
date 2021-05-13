def main():
    S = str(input())
    ls = len(S)

    for i in range(ls):
        for j in range(i, ls):
            if S[:i] + S[j:] == 'keyence':
                return 'YES'
    return 'NO'

print(main())
