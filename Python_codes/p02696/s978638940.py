import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def f(x, a, b):
    return ((a*x)//b) - (a*(x//b))

def main():
    a, b, n = map(int, readline().split())
    if n < b:
        print(f(n, a, b))
    else:
        print(f(b-1, a, b))
if __name__ == '__main__':
    main()
