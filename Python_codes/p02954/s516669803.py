S = input()


def solve(s):
    buf = [1] * len(s)

    for i in range(len(buf) - 2):
        if s[i] == "R" and s[i + 1] == "R":
            buf[i+2] += buf[i]
            buf[i] = 0

    for i in range(len(buf) - 1, 1, -1):
        if s[i] == "L" and s[i - 1] == "L":
            buf[i-2] += buf[i]
            buf[i] = 0

    return " ".join(map(str, buf))


print(solve(S))
