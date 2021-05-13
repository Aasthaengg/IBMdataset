def agc012a_atCoder_group_contest():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    total = 0
    for i in range(n):
        a.pop()
        total += a.pop()
    print(total)

agc012a_atCoder_group_contest()