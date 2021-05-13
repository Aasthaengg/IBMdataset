def main():
    n, a, b, c, d = map(int,input().split())
    s = list(input())
    if c<d:
        for i in range(a-1,c-2):
            if s[i] == s[i+1] and s[i] == '#':
                print('No')
                return
        for i in range(b-1,d-2):
            if s[i] == s[i+1] and s[i] == '#':
                print('No')
                return
        print('Yes')
    else:
        for i in range(a-1,c-2):
            if s[i] == s[i+1] and s[i] == '#':
                print('No')
                return
        for i in range(b-1,d-2):
            if s[i] == s[i+1] and s[i] == '#':
                print('No')
                return

        for i in range(b-1,d):
            if s[i-1] == s[i] == s[i+1] and s[i] == '.':
                print('Yes')
                return


        print('No')



if __name__ == '__main__':
    main()
