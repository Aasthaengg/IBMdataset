import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    a,b,c,d = map(int, readline().split())
    ans = max(a*c, a*d, b*c, b*d)
    print(ans)
if __name__ == '__main__':
    main()
