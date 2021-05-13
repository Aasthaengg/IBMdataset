import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def f(a, b, c):
    if (a%2 != 0) | (b%2 != 0) | (c%2 != 0):
        return 0
    if (a == b) & (b == c):
        return -1
    return f((b+c)//2, (a+c)//2, (a+b)//2) + 1
def main():
    a, b, c = map(int, readline().split())
    print(f(a, b, c))
if __name__ == '__main__':
    main()
