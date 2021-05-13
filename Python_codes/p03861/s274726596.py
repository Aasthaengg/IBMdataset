a, b, x = list(map(int, input().split()))
def num_dev(n, x):
    if n == -1: return 0
    return n // x + 1
print(num_dev(b, x) - num_dev(a - 1, x))