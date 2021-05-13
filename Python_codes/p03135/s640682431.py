def main():
    from sys import stdin
    r = stdin.readline()[:-1]
    #r = stdin.readlines()

    a, b = map(int, r.split())
    print(a/b)
    
if __name__ == '__main__':
    main()

