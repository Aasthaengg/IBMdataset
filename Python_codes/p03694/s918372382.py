N = int(input())

a = list(set(sorted([int(x) for x in input().split()])))

print(max(a)-min(a))