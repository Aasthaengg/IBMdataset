import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def main():
    N = int(readline())
    print((N*(N-1))//2)
if __name__ == '__main__':
    main()
