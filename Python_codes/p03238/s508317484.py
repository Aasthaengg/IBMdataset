def main():
    from sys import stdin
    #r = stdin.readline()[:-1]
    n = int(stdin.readline()[:-1])   
    #r = [stdin.readline() for i in range(n)]
    #t = [int(stdin.readline()) for i in range(n)]

    if n == 1:
        print('Hello World')
    else:
        r = [int(stdin.readline()) for i in range(n)]
        print(r[0] + r[1])
   
if __name__ == '__main__':
    main()

