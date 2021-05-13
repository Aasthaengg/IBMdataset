
def resolve():
    def decode(x):
        return ord(x) - 97

    def encode(x):
        return chr(x + 97)

    S = list(map(decode, input()))
    K = int(input())

    for i in range(len(S) - 1):
        if S[i] == 0:
            continue
        if 26 - S[i] <= K:
            K -= 26 - S[i]
            S[i] = 0

    S[-1] = (S[-1] + K) % 26
    ans = map(encode, S)
    print("".join(ans))


if __name__ == "__main__":
    resolve()