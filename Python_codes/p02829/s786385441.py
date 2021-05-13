import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    ab = [int(input()) for _ in range(2)]
    for i in range(1,4):
        if i not in ab:
            print(i)
            return

if __name__ == '__main__':
    main()