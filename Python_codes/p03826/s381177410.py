def main():
    a,b,c,d = (int(x) for x in input().split())
    print(max(a*b,c*d))

if __name__ == '__main__':
    main()