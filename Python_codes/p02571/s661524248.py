def main():
    s = (input())
    # d,t,s = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    t = (input())

    mn = 10**5
    for i in range(len(s)-len(t)+1):
        result = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                result += 1
        mn = min(result, mn)

    print(mn)


if __name__ == '__main__':
    main()
