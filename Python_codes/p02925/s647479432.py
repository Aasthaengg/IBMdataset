n = int(input())
A = [list(int(x) - 1 for x in input().split()) for _ in range(n)]
B = [0] * n

ans = 1
stack = [i for i in range(n)]
while True:
    day_set = set()
    next_stack = []
    while stack:
        i = stack.pop()
        if i in day_set or B[i] >= n - 1:
            continue
        j = A[i][B[i]]
        if j in day_set or B[j] >= n - 1:
            continue
        if A[j][B[j]] == i:
            B[i] += 1
            B[j] += 1
            day_set.add(i)
            day_set.add(j)
            next_stack += [i, j]
            if all(b >= n - 1 for b in B):
                print(ans)
                exit()

    if not day_set:
        print(-1)
        exit()
    ans += 1
    stack = next_stack
