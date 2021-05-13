import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    S = readline().strip()

    S = S.replace("?", "D")

    print(S)


if __name__ == "__main__":
    main()
