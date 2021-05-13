import sys
input = sys.stdin.readline

def main():
    a = int(input())
    s = input().strip()

    if a >= 3200:
        print(s)
    else:
        print('red')


if __name__ == "__main__":
    main()
