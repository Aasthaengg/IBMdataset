def main():
    N, M = (int(i) for i in input().split())
    S = input()
    from itertools import groupby
    for k, v in groupby(S):
        if k == "1" and M <= len(list(v)):
            return print(-1)
    ans = []
    posi = 0
    S = S[::-1]
    while posi < N:
        pre = posi
        posi = min(posi+M, N)
        while S[posi] == "1":
            posi -= 1
        ans.append(posi - pre)
    print(*(ans[::-1]))


if __name__ == '__main__':
    main()
