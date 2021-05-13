N = int(input())
print(sum(sorted([int(x) for x in input().strip().split()], reverse=True)[1:2*N:2]))