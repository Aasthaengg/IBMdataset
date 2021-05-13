n, x = map(int, input().split())
m = sorted([int(input()) for _ in range(n)])
print((x-sum(m))//m[0]+n)