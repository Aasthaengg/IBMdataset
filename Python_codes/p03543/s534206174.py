def main():
    n = list(input())
    if n.count(n[1]) >= 3 and n[1]==n[2]: print('Yes')
    else: print('No')

if __name__ == '__main__':
    main()