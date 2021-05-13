import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    s = str(readline().rstrip().decode('utf-8'))
    cnt = 0
    for i in range(len(s)):
        if cnt == 0:
            if s[i] == "C":
                cnt += 1
        elif cnt == 1:
            if s[i] == "F":
                print("Yes")
                exit()
    print("No")


if __name__ == '__main__':
    solve()
