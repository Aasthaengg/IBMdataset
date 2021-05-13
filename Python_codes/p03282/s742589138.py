import sys
def input(): return sys.stdin.readline().strip()

def main():
    S = input()
    K = int(input())

    for i in range(K):
        n = int(S[i])
        if n != 1:
            print(n)
            return
    print(1)


if __name__ == "__main__":
    main()
