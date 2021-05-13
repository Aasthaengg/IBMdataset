def r_t(n):
    return sum(map(int, n.split()))%24
print(r_t(input()))