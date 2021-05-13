def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
    #r = stdin.readline()[:-1]
    #n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]
    t = [int(stdin.readline()) for i in range(4)]

    #res = 0
    #a, b, c = map(int, r.split())
    print(min(t[0],t[1])+min(t[2],t[3]))

if __name__ == '__main__':
    main()

