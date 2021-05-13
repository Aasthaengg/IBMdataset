def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    itv = []
    for i in range(n):
        x, l = map(int, input().split())
        itv.append((x+l, x-l))
    itv.sort()
    r = - 10 ** 12
    cnt = 0
    for x in itv:
        if r <= x[1]:
            cnt += 1
            r = x[0]
    
    print(cnt)

    
    
if __name__ == '__main__':
    main()