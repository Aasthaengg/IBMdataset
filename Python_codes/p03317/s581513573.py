import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    n, k = map(int, readline().split())
    print((((n-k)+(k-1)-1)//(k-1))+1)
if __name__ == '__main__':
    main()
