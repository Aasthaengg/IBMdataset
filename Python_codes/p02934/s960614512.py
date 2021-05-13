def resolve():
    N = int(input().strip())
    array = list(map(int, input().strip().split(' ')))
    rev_sum = 0
    for i in range(N):
        rev_sum = rev_sum + (1/array[i])
    ans = 1/rev_sum
    print(ans)
resolve()
