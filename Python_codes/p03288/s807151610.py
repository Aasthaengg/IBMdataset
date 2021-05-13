def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
    r = stdin.readline()[:-1]
    #n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]

    r = int(r)
    if r < 1200:
        print('ABC')
    elif r < 2800:
        print('ARC')
    else:
        print('AGC')

if __name__ == '__main__':
    main()

