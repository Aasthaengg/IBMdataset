def abc153d_caracal_vs_monster():
    h = int(input())
    cnt = 0
    result = 0
    while h > 0:
        h = h//2
        result += pow(2, cnt)
        cnt += 1
    print(result)
abc153d_caracal_vs_monster()