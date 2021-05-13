def main():
    n = int(input())
    s = input().split()
    print('Four') if len(set(s)) == 4 else print('Three')

if __name__ == '__main__':
    main()
