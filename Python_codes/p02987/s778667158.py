import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    s = input().strip()
    a = s[0] ; b = None
    c = 1 ; d = 0

    for i in range(1, 4):
        if s[i] == a:
            c += 1

        elif b == None:
            b = s[i]
            d += 1

        elif s[i] == b:
            d += 1

    if c == 2 and d == 2:
        print('Yes')
    else:
        print('No')

main()