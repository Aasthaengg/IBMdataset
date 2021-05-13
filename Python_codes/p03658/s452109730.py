_, k = map(int, input().split())
l = [int(x) for x in input().split()]
l.sort()
print(sum(l[-k:]))