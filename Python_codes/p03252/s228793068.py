def main():

    S = list(input())
    T = list(input())

    d = dict()
    d_inv = dict()
    for i in range(len(S)):
        if S[i] not in d:
            if T[i] in d_inv:
                return "No"
            else:
                d[S[i]] = T[i]
                d_inv[T[i]] = S[i]
        else:
            if d[S[i]] != T[i]:
                return "No"
    return "Yes"
        
if __name__ == '__main__':
    print(main())
