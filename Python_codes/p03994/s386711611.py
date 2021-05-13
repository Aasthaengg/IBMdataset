import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input())
    k = int(input())
    alphabet = [chr(i) for i in range(97, 97 + 26)]

    for i in range(len(s)):
        if s[i] == "a":
            continue

        idx = alphabet.index(s[i])
        if 26 - idx <= k:
            s[i] = "a"
            k -= 26 - idx

    if k:
        idx = alphabet.index(s[i]) + k % 26
        s[-1] = alphabet[idx]

    print("".join(s))



if __name__ == '__main__':
    resolve()
