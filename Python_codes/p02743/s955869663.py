def main():
    a,b,c  = map(int,(input().split()))

    if c-a-b <0:
        print('No')
    elif 4*a*b - (c-a-b)**2 < 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
