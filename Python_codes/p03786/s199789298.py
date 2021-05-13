def agc011_b():
    N = int(input())
    A = sorted([0] + list(map(int, input().split())))

    cumsum = [0]
    for i in range(1, N+1):
        cumsum.append(cumsum[-1] + A[i])

    ans = 1
    for i in range(N-1, 0, -1):
        if cumsum[i] * 2 < A[i+1]:
            break  # 2倍しても次に小さい個体を吸収できないので、これ以下は生き残れない
        else:
            ans += 1
    print(ans)

agc011_b()