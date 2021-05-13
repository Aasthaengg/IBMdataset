N = int(input())
L = list(map(lambda l: int(l), input().split(" ")))
L.sort()

print("Yes") if L[-1] < sum(L[:-1]) else print("No")