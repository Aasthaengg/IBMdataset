import sys
def input(): return sys.stdin.readline().strip()


def main():
    s = input()
    d = set()
    for c in s:
        if c in d:
            print("no")
            return
        d.add(c)
    print("yes")

if __name__ == "__main__":
    main()
