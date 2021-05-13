def main():
    a,b = (int(x) for x in input().split())
    print(a if a<=b else a-1)

if __name__ == '__main__':
    main()