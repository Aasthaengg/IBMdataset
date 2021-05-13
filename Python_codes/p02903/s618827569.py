def main():
    H, W, A, B = (int(i) for i in input().split())
    for i in range(B):
        print("0"*A+"1"*(W-A))
    for i in range(H-B):
        print("1"*A+"0"*(W-A))


if __name__ == '__main__':
    main()
