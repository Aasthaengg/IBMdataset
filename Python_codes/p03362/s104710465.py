def main():
    import sys
    input = sys.stdin.readline
    isprime = [True if i % 2 else False for i in range(55555+1)]
    isprime[1] = False
    rem = 1
    ans = []
    for i, j in enumerate(isprime[2:], start=2):
        if not j:
            continue
        ind = i * 2
        while ind <= 55555:
            isprime[ind] = False
            ind += i

    for i, j in enumerate(isprime):
        if not j:
            continue
        if i % 5 == rem:
            ans.append(i)
    
    print(*ans[:int(input())])

if __name__ == '__main__':
    main()