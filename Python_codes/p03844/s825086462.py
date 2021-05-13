def main():
    a,op,b = (x for x in input().split())
    if op == '+': print(int(a)+int(b))
    else: print(int(a)-int(b))

if __name__ == '__main__':
    main()