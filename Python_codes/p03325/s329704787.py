import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def numOftwo(x):
    cnt = 0
    while x%2 == 0:
        x //= 2
        cnt += 1
    return cnt

def main():
    N = int(readline())
    a = [int(i) for i in readline().split()]
    s = 0
    for i in range(N):
        s += numOftwo(a[i])
    print(s)
if __name__ == '__main__':
    main()
