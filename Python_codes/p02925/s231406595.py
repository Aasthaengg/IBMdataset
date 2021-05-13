def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.buffer.readline

    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    adj = defaultdict(list)
    in_num = defaultdict(int)
    for i in range(N):
        for j in range(N-2):
            x1 = x2 = i+1
            y1 = A[i][j]
            y2 = A[i][j+1]
            if x1 > y1:
                x1, y1 = y1, x1
            if x2 > y2:
                x2, y2 = y2, x2
            adj[x1*(N+1)+y1].append(x2*(N+1)+y2)
            in_num[x2*(N+1)+y2] += 1
    st = []
    ng = (N * (N - 1)) // 2
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if in_num[i*(N+1)+j] == 0:
                st.append(i*(N+1)+j)
                ng -= 1
    ans = 0
    while st:
        ans += 1
        st_new = []
        for par in st:
            for child in adj[par]:
                if in_num[child] == 1:
                    st_new.append(child)
                    ng -= 1
                in_num[child] -= 1
        if st_new:
            st = st_new
        else:
            break

    if ng:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
