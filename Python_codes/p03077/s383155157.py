import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    n, *data = map(int, readlines())
    d = [int(i) for i in data]
    mi = min(d)
    mx = max(d)
    if mi > n:
        print(5)
        return
    n = (n+mi-1)//mi
    print(n+4)
if __name__ == '__main__':
    main()
