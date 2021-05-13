import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N = int(readline())
    A = [int(i) for i in readline().split()]
    s = 0
    for i in range(1, N):
        pre = A[i-1] #前の人の身長
        now = A[i] #今見ている身長
        if pre > now:
            step = pre-now
            s += step
            A[i] += step
    print(s) 
if __name__ == '__main__':
    main()
