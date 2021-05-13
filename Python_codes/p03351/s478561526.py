def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
    r = stdin.readline()[:-1]
    #n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]

    res = 0
    a, b, c, d = map(int, r.split())
    if abs(b-a) <= d and abs(c-b) <= d or abs(c-a) <= d:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

