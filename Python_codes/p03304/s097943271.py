def mean_beauty(n, m, d):
    if d == 0:
        prob = 1/n
    else:
        prob = 2*(n - d)/n**2

    return prob * (m-1)

n, m, d = map(int, input().split())

print(mean_beauty(n, m, d))
