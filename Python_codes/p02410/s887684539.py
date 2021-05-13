n, m = map(int, input().split())
a = [[v for v in list(map(int, input().split()))] for i in range(n)]
b = [int(input()) for i in range(m)]
c = [sum([a[i][j] * b[j] for j in range(m)]) for i in range(n)]
print('\n'.join(map(str, c)))