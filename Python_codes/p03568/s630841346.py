n = int(input())
l = [int(i) for i in input().split()]

l = [i for i in l if i % 2 == 0]

print(3 ** n - 2 ** len(l))