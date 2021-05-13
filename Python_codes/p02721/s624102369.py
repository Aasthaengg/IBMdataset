def main():
    N, K, C = map(int, input().split())
    S = input()
    ansL = [0] * K
    pos = 0
    idx = 0
    while idx < K:
        if S[pos] == "o":
            ansL[idx] = pos
            idx += 1
            pos += C + 1
        else:
            pos += 1
    ansR = [0] * K
    pos = N-1
    idx = K-1
    while idx >= 0:
        if S[pos] == "o":
            ansR[idx] = pos
            idx -= 1
            pos -= C + 1
        else:
            pos -= 1
    for i in range(K):
        if ansL[i] == ansR[i]:
            print(ansL[i] + 1)


if __name__ == "__main__":
    main()
