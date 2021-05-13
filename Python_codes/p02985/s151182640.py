import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().split())

    mod = 10 ** 9 + 7

    roots = [[] for _ in range(n)]
    for i in range(n-1):
        a,b = map(int,input().split())
        roots[a-1].append(b-1)
        roots[b-1].append(a-1)

    li = [-1] * n
    li[0] = k
    ans = 1
    stack = [0]

    while stack:
        label = stack.pop(-1)
        count = 1
        li2 = []
        for i in roots[label]:
            if li[i] == -1:
                stack.append(i)
                li2.append(i)
            else:
                count += 1
        for i in li2:
            li[i] = k - count
            count += 1

    for i in li:
        ans *= max(i,0)
        ans %= mod

    print(ans)

if __name__ == '__main__':
    main()
