def main():
    t = list(map(int, input().split()))
    if sum(t[0:2]) == t[2] or sum(t[1:]) == t[0] or sum(t[::2]) == t[1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()