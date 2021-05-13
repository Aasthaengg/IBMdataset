def main():
    S = input()
    N = len(S)
    K = int(input())
    from string import ascii_lowercase
    dic = {a: i for i, a in enumerate(ascii_lowercase)}
    rdic = {i: a for i, a in enumerate(ascii_lowercase)}
    li = [(26 - dic[s]) % 26 for s in S]
    ans = []
    # print(li)
    for i, cnt in enumerate(li):
        if i == N - 1:
            ans.append(rdic[(dic[S[i]] + K) % 26])
            continue
        if cnt <= K:
            K -= cnt
            ans.append("a")
        else:
            ans.append(S[i])
    print("".join(ans))


if __name__ == '__main__':
    main()
