from collections import defaultdict

def main():
    X,Y = [int(x) for x in input().split()]
    ans = 0
    while X<=Y:
        X *= 2
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
