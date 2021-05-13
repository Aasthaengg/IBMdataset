n, k = map(int, input().split())
p = [int(i) for i in input().split()]
print(sum(sorted(p)[:k]))