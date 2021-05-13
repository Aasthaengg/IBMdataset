import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    S =input()
    N = len(S)
    one = S.count("1")
    zero = N-one
    print(min(zero,one)*2)



if __name__ == "__main__":
    main()
