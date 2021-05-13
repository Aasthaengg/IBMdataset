N = int(input())
D = sorted([int(x) for x in input().split()])
print(D[len(D)//2]-D[(len(D)//2)-1])