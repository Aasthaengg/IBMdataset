def main():
    n = int(input())
    s, t = input().split()
    ans = list()
    for i, j in zip(s, t):
        ans.append(i)
        ans.append(j)
    print(*ans, sep='')

if __name__ == '__main__':
    main()
