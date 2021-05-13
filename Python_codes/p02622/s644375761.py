import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    s = input()
    t = input()
    r = 0
    for se, te in zip(s, t):
        r += se != te
    print(r)


if __name__ == '__main__':
    main()