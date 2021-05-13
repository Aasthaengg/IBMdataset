def main():
    a,b = input().split()
    ans = ''
    if a == 'H':
        ans = b
    else:
        ans = 'H' if b == 'D' else 'D'
    print(ans)


if __name__ == '__main__':
    main()