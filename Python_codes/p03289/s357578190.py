import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = list(ns())
    if S[0] == 'A' and 'C' in S[2:-1]:
        S.remove('A')
        S.remove('C')
        for s in S:
            if s.isupper():
                print('WA')
                return
        print('AC')
    else:
        print('WA')


if __name__ == '__main__':
    main()
