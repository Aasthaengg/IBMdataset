n = int(input())
V = list(map(int, input().split()))
a = V[0]

print(sum([i**(-1) for i in V])**(-1))