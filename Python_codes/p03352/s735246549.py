def main():
    X = int(input())
    ans = 1
    for b in range(1,X+1):
        for p in range(2,10):
            a = b**p
            if a > X:
                break
            elif ans < a and a <= X:
                ans = a
            # print(b,p,a,ans)
    print(ans)

if __name__ == '__main__':
    main()