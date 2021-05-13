def main():
    n =  int(input())
    ls = []
    for _ in range(n):
        a, b = map(int, input().split())
        ls.append([b,a])
    ls.sort()
    t=0
    for i in ls:
        t += i[1]
        if t > i[0]:
            print('No')
            exit(0)
    print('Yes')
if __name__ == '__main__':
    main()