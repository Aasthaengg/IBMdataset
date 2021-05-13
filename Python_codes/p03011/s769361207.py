n = [int(n) for n in input().split()]
n.remove(max(n))
print(sum(n))