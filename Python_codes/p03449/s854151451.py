N = int(input())
A = [input().split() for i in range(2)]
A = [[int(s) for s in row] for row in A]
numberOfCandies = []

for i in range(N):
    candies = 0
    for j in range(i+1):
        candies+=A[0][j]
    for j in range(i,N):
        candies+=A[1][j]
    numberOfCandies.append(candies)

print(max(numberOfCandies))