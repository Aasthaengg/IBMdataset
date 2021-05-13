def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
    r = stdin.readline()[:-1]
    #n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]

    a, b = map(int, r.split())
    if a%b == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()

