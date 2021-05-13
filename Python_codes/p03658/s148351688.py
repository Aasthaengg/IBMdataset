n, k = map(int, input().split())
l = [int(ln) for ln in input().split()]
l.sort(reverse=True)
print(sum(l[:k]))