N = int(input())
cost = [int(input()) for i in range(5)]

minc = min(cost)

print((N-1)//minc + 5)