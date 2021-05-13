def main():
    from sys import stdin
    r = stdin.readline()[:-1]
    #r = stdin.readlines()

    a, b = map(int, r.split())
    if b%a == 0:
        print(a+b)
    else:
        print(b-a)
    
if __name__ == '__main__':
    main()

