import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    a = int(readline())
    s = readline().strip()

    if a >= 3200:
        print(s)
    else:
        print("red")


if __name__ == "__main__":
    main()
