n = int(input())
a = [int(x) for x in input().split()]
print(sum([(x - round(sum(a) / n))**2 for x in a]))