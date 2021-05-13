
def resolve():
    S = input()
    K = int(input())

    ans = []
    for s in S:
        diff = ord(s) - ord("a")
        if diff == 0:
            ans.append("a")
            continue
        elif 26 - diff <= K:
            ans.append("a")
            K -= 26 - diff
        else:
            ans.append(s)

    K %= 26
    d = (K + ord(ans[-1]) - ord('a')) % 26
    ans[-1] = chr(d + ord('a'))

    print("".join(ans))


if __name__ == "__main__":
    resolve()