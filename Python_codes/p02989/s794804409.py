n = int(input())
D = list(map(int, input().strip().split()))

D.sort()
m = int(len(D)/2)
print(D[m] - D[m - 1])
