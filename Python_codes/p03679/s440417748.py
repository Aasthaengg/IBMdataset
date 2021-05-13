def main():
    x,a,b = (int(x) for x in input().split())
    if b <= a: print('delicious')
    elif b-a <= x: print('safe')
    else: print('dangerous')

if __name__ == '__main__':
    main()