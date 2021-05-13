def log2(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    return cnt


N = int(input())
print(sum(map(lambda x: log2(int(x)), input().split())))