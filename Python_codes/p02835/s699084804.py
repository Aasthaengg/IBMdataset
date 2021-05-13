def main():
    A = list(map(int, input().split()))
    print('win' if sum(A) <= 21 else 'bust')

if __name__ == '__main__':
    main()

