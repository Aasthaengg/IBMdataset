import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    m = [0]*N
    for _ in range(M):
        a, b = map(int, input().split())
        m[a-1] += 1
        m[b-1] += 1
    for i in range(N):
        print(m[i])

if __name__ == '__main__':
    main()