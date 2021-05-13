def main():
    a,b,c=input().split(' ')
    if a[-1] == b[0] and b[-1] == c[0]:
        print('yes'.upper())
    else:
        print('no'.upper())

if __name__ == '__main__':
    main()