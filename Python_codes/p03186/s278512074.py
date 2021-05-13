def main():
    A,B,C = map(int,input().split())
    ans = min(A+B+1,C) + B
    print(ans)

if __name__ == '__main__':
    main()