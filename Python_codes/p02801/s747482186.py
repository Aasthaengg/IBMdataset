import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    c = readline().strip()

    print(chr(ord(c) + 1))


if __name__ == "__main__":
    main()
