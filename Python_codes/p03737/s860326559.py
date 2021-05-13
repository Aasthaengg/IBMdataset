import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    words = list(input().split())
    print((words[0][0]+words[1][0]+words[2][0]).upper())

if __name__ == '__main__':
    main()