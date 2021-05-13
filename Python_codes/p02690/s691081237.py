import sys
input = sys.stdin.readline
def main():
    X = int(input())
    for i in range(-120, 121):
        for j in range(-120, 121):
            if i**5 - j **5 == X:
                print(i, j)
                return

if __name__ == '__main__':
    main()