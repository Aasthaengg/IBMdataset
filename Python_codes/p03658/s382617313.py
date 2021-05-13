# ABC 067: B – Snake Toy
n, k = map(int, input().split())
l = [int(s) for s in input().split()]
l.sort()
print(sum(l[k * (-1):]))