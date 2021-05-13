def main():
    import sys
    input = sys.stdin.readline
    N, M = [int(x) for x in input().strip().split()]
    l = [0] * N
    for m in range(M):
        a, b = [int(x) for x in input().strip().split()]
        l[a-1] += 1
        l[b-1] += 1
    if [i for i in l if i % 2]:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()