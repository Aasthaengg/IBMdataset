N = int(input())
K = int(input())
x = [int(x) for x in input().split()]

moveSum = 0
for x2 in x:
    move = x2 * 2
    if move > (K - x2) * 2:
        move = (K - x2) * 2
    moveSum += move

print(moveSum)