def main():
    h = int(input())
    ans = 1
    if h >= 1:
        i = 0
        while 2**i <= h:
            ans = 2**(i+1) - 1
            i += 1
    print(ans)

if __name__ == '__main__':
    main()
