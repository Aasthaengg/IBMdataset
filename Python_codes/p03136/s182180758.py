N=input()
sides = [int(i) for i in input().split()]
maxSide = max(sides)
print('Yes' if maxSide < sum(sides) - maxSide else 'No')