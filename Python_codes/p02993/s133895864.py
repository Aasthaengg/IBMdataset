def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    s = input().strip()

    if s[0] == s[1]:
        print('Bad')
        exit()

    if s[1] == s[2]:
        print('Bad')
        exit()

    if s[2] == s[3]:
        print('Bad')
        exit()

    print('Good')


main()


