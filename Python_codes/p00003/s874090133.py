for _ in range(int(input())):
    datasqr = [i ** 2 for i in sorted(list(map(int, input().split())))]
    print('YES' if sum(datasqr[:2]) == datasqr[-1] else 'NO')
