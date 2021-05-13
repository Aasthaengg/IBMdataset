def nikkei19q_a():
    N, A, B = map(int, input().split())
    ans_max = min(A, B)
    ans_min = max(0, A + B - N)
    print(*[ans_max, ans_min], sep=' ')

nikkei19q_a()