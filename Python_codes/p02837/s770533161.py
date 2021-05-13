def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())

    tf = [[] for _ in range(n)]
    for i in range(n):
        a = int(input())
        for j in range(a):
            x, y = map(int, input().split())
            tf[i].append((x-1, y))

    ans = 0
    for i in range(1 << n):
        tmp = format(i, 'b').count('1')
        for j in range(n):
            if (i>>j)&1:
                for x, y in tf[j]:
                    if (i>>x)&1 != y:
                        break
                else:
                    continue
                break
        else:
            ans = max(ans, tmp)
    print(ans)


            



if __name__ == '__main__':
    main()