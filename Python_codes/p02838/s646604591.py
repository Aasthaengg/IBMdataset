import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    n = int(readline())
    a = [int(i) for i in readline().split()]
    s = 0
    P = int(1e9)+7
    for k in range(60):
        cnt = 0    
        for e in a:
            if (e>>k) & 1:
                cnt += 1
        s += cnt*(n-cnt)*pow(2, k, P)
        s %= P
    print(s)
if __name__ == '__main__':
    main()
