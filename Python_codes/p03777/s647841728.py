def main():
    a,b = (True if x=='H' else False for x in input().split())
    if (a and b) or (not a and not b): print('H')
    else: print('D')

if __name__ == '__main__':
    main()