import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    a = list(input())
    K = int(input())
    for i in range(len(a)):
        if a[i]=='a':
            val=0
        else:
            val = 123 - ord(a[i])

        if val <= K:
            a[i] = 'a'
            K -= val
        if i == len(a) - 1 and K > 0:
            a[-1] = chr(ord(a[-1]) + K % 26)
    print(''.join(a))


resolve()