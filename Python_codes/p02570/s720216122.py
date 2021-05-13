import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    D, T, S = map(int, readline().split())
    if T*S >= D:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()
