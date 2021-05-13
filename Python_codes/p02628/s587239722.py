n, k = map(int, input().split())
p = [int(s) for s in input().split()]
sum = 0

for i in range(k):
    sum += min(p)
    p.remove(min(p))
print(sum)