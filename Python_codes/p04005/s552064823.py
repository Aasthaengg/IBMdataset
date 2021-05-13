import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    a, b, c = map(int, readline().split())
    if (a*b*c)%2 == 0:
        print(0)
    else:
        #すべて奇数
        print(min((a*b, b*c, c*a)))
if __name__ == '__main__':
    main()
