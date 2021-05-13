import sys

input = sys.stdin.readline

def main():
    ans = 0
    n, m = map(int, input().split())
    all = []
    for i in range(n):
        all.append(list(map(int, input().split())))
    all.sort()
    for i in range(n):
        if m >= all[i][1]:
            m -= all[i][1]
            ans += all[i][0]*all[i][1]
        else:
            ans += all[i][0]*(m)
            break
    print(ans)

if __name__ == '__main__':
    main()