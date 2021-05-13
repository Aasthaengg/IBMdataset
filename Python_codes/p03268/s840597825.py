def main():
    N, K = map(int, input().split())
    if K % 2 == 1:
        print((N//K)**3)
    else:
        e = N//K
        o = ((N//(K//2))+1)//2
        print(e**3 + o**3)

if __name__ == '__main__':
    main()
