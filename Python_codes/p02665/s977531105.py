import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    maxnum = [0] * (n + 1)
    num = [0] * (n + 1)
    maxnum[0] = 1
    num[0] = 1
    if n > 0:
        num[-1] = a[-1]

    if n == 0 and a[0] == 1:
        print(1)
    elif n == 0 and a[0] == 0:
        print(-1)
    elif n == 0 and a[0] > 1:
        print(-1)
    elif n >= 1 and a[0] > 0:
        print(-1)
    elif n == 1 and a[1] == 1:
        print(2)
    elif n == 1 and a[1] == 2:
        print(3)
    else:
        for i1 in range(1, n + 1):
            if maxnum[i1-1] * 2 < a[i1]:
                print(-1)
                sys.exit()
            else:
                maxnum[i1] = maxnum[i1-1] * 2 - a[i1]

        for j1 in range(n-1, 0, -1):
            numt = a[j1] + min(num[j1 + 1], maxnum[j1-1]*2 - a[j1])
            num[j1] = numt
        r = sum(num)
        print(r)

if __name__ == '__main__':
    main()

