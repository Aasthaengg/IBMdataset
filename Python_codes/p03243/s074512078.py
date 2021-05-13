def main():
    N = int(input())
    for i in range(1, 10):
        if int(str(i) * 3) >= N:
            print(str(i) * 3)
            break

if __name__ == '__main__':
    main()
