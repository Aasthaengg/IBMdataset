def resolve():
    n = int(input())
    a_1 = list(map(int, input().split()))
    a_2 = list(map(int, input().split()))
    total = 0
    for i in range(n):
        line_1 = sum(a_1[:i+1])
        line_2 = sum(a_2[i:])
        total = max(total, line_1+line_2)
    print(total)
resolve()