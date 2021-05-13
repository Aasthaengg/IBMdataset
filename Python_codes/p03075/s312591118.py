import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    abcde = [int(input()) for _ in range(5)]
    k = ni()
    for i in range(5):
        for j in range(i, 5):
            if k < abs(abcde[i] - abcde[j]):
                print(':(')
                return
    print('Yay!')


if __name__ == '__main__':
    main()
