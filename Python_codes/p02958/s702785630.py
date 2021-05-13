import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    p = list(map(int, input().split()))
    check = [i for i in range(1, n+1)]
    cnt = 0
    for a, b in zip(p, check):
        if a != b:
            cnt += 1
    if cnt == 0 or cnt == 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()