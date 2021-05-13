def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
    r = stdin.readline()[:-1]
    #n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]

    res = 0
    a, b, c = map(int, r.split())
    if a+b < c or a > c:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()

