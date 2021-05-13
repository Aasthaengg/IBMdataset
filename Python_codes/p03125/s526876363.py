def main():
    A, B = map(int, input().split())
    if B % A == 0: return A+B
    else: return B- A

if __name__ == '__main__':
    print(main())