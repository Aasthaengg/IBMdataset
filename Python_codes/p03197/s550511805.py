def main():
    N, *A = map(int, open(0).read().split())
    ans = 'second'
    for a in A:
        if a % 2 == 1:
            ans = 'first'
    print(ans)

if __name__ == '__main__':
    main()
