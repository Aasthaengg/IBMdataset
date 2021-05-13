import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))

    if a.count(0) == n:
        print("Yes")
    else:
        if n % 3 == 0:
            s = list(set(a))
            if len(s) == 3:
                if s[0] ^ s[2] == s[1] and s[1] ^ s[0] == s[2] and s[2] ^ s[1] == s[0]:
                    if a.count(s[0]) == a.count(s[1]) == a.count(s[2]):
                        print("Yes")
                    else:
                        print("No")
                else:
                    print("No")
            elif len(s) == 2:
                if a.count(0) == n // 3:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")


if __name__ == '__main__':
    main()
