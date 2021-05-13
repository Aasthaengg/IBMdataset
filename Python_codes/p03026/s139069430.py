def main():

    N = int(input())
    count = [[] for i in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        count[a-1].append(b-1)
        count[b-1].append(a-1)

    max_l = 0
    max_i = -1
    for i in range(N):
        if len(count[i]) > max_l:
            max_l = len(count[i])
            max_i = i

    c = list(map(int, input().split()))
    c.sort(reverse = True)
    # print(c)

    cur = [max_i]
    val = [0 for _ in range(N)]
    i = 0
    val[max_i] = c[i]
    i += 1
    ans = 0
    while cur:
        temp = []
        for j in cur:
            for k in count[j]:
                if val[k] == 0:
                    val[k] = c[i]
                    ans += c[i]
                    i += 1
                    temp.append(k)
        cur = temp

    print(ans)
    print(" ".join(map(str, val)))

if __name__ == '__main__':
    main()