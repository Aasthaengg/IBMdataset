import string


def solution(s):
    if len(s) == 0:
        for c in string.ascii_lowercase:
            if S[0] < c:
                print(c)
                return
        print(-1)
        return

    for c in string.ascii_lowercase:
        if len(s + c) == len(set(s + c)) and (s + c) > S:
            print(s + c)
            return
    solution(s[:-1])


if __name__ == "__main__":

    S = input()
    solution(S)
