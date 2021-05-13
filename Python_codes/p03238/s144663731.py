def main():
    N = int(input())
    if N == 1:
        print("Hello World")
    else:
        num = [int(input()) for i in range(2)]
        print(num[0]+num[1])
if __name__ == "__main__":
    main()