import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    D = list(input())
    dic = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    ans = []
    for d in D:
        ans.append(dic[d])
    print(''.join(ans))


if __name__ == '__main__':
    main()
