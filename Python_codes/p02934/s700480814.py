n = int(input())
V = list(map(int, input().split()))
a = V[0]

print(1/sum([1/i for i in V]))