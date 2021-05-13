def abc148d_brick_break():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    val = 1
    for item in a:
        if item == val:
            val += 1
        else:
            cnt += 1
    if val == 1:
        print('-1')
    else:
        print(cnt)
abc148d_brick_break()