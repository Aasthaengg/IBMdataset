n = int(input())
a = [int(i) for i in input().split()]
print(1 / sum(1 / ai for ai in a))