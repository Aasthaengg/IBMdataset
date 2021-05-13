def main():
    A, B, C = map(int, input().split())
    return B + min(C, A+B+1)

if __name__ == '__main__':
    print(main())