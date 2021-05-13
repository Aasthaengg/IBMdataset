import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def dist(x, y): 
    return (x**2+y**2)**0.5
def main():
    N, D = map(int, readline().split())
    cnt = 0
    for _ in range(N):
        x, y = map(int, readline().split())     
        if dist(x, y) <= D:
            cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()
