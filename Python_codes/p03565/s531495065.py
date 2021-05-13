def main():
    S = input()
    T = input()
    n = len(T)
    ans = list(S)
    for i in range(len(S) - n, -1, -1):
        s = S[i:i + n]
        for j, t in zip(s, T):
            if j != '?' and j != t:
                break
        else:
            ans[i:i + n] = list(T)
            ans = [a if a != '?' else 'a' for a in ans]
            print(''.join(ans))
            exit()
    print('UNRESTORABLE')



if __name__ == '__main__':
    main()
