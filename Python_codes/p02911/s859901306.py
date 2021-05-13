def resolve():
    n, k, q = map(int, input().split())
    score = [0] * n
    for _ in range(q):
        a = int(input())
        score[a-1] += 1
    for i in range(n):
        s = k + score[i] - q
        if s > 0:
            print("Yes")
        else:
            print("No")
resolve()