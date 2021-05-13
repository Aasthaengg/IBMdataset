import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    c = ord(input())
    print(chr(c+1))

if __name__ == '__main__':
    main()