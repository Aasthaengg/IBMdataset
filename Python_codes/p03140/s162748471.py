def main():
    n = int(input())
    A = input()
    B = input()
    C = input()
    ans = 0
    for a in zip(A, B, C):
        if len(set(a)) == 2:
            ans += 1
        elif len(set(a)) == 3:
            ans += 2
    print(ans)

if __name__ == '__main__':
    main()
