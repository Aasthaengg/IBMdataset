import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    k = int(input())
    if k >= len(s):
        for i in range(len(s)):
            if s[i] != "1":
                print(s[i])
                break
        else:
            print(1)
    else:
        for i in range(k):
            if s[i] != "1":
                print(s[i])
                break
        else:
            print(1)


if __name__ == '__main__':
    resolve()
