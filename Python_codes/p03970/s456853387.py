def main():
    S = input()
    C = 'CODEFESTIVAL2016'
    ans = 0
    for s, c in zip(S, C):
        if s != c:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
