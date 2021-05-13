def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
    r = stdin.readline()[:-1]
    #n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]

    res = 0
    a, b = map(int, r.split())
    print(max(a+b,a-b,a*b))

if __name__ == '__main__':
    main()

