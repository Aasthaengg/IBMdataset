import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    w, h, x, y = map(int, readline().split())
    ans = '{:.10f}'.format(w*h/2) 
    print(ans, end=' ')
    if (2*x == w) and (2*y == h):
        print(1)
    else:
        print(0)
if __name__ == '__main__':
    main()