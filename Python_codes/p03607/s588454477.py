import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    d = set()
    for _ in range(N):
        a = int(input())
        if a in d:
            d.remove(a)
        else:
            d.add(a)
    print(len(d))



if __name__ == "__main__":
    main()
