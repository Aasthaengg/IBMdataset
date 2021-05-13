def main():
    t = list(map(int, input().split()))
    t.sort()
    print(t[0] + t[1])

if __name__ == '__main__':
    main()