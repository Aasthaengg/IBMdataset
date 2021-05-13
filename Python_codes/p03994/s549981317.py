import sys
input = sys.stdin.readline


def read():
    s = input().strip()
    K = int(input().strip())
    return s, K


def solve(s, K):
    ans = []
    for a in s:
        c = (ord("z") - ord(a) + 1) % 26
        if c <= K:
            K -= c
            ans.append("a")
        else:
            ans.append(a)
    if K > 0:
        c = (ord(ans[-1]) - ord("a") + K) % 26
        ans[-1] = chr(c + ord("a"))
    return "".join(ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
