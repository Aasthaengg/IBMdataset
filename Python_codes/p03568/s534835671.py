n = int(input())
a = [int(x) % 2 for x in input().split()]
print(3**len(a) - 1) if sum(a) == len(a) else print(3**len(a) - 2**(len(a) - sum(a)))