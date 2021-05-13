def main():
    N = int(input())
    A = [int(_) for _ in input().split()]
    xor = 0
    for a in A:
        xor ^= a
    print('No' if xor else 'Yes')
    return

if __name__ == '__main__':
    main()
