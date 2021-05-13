def main():
    S = input()
    c = False
    for s in S:
        if s == 'C':
            c = True
        if c and s == 'F':
            print('Yes')
            exit()
    print('No')
if __name__ == '__main__':
    main()
