import sys
def input(): return sys.stdin.readline().strip()


def main():
    s = input()
    t = input()
    for i, c in enumerate(s):
        if t[-i-1] != c:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()
