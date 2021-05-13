N = int(input())
houses = [int(i) for i in input().split()]

print(max(houses)-min(houses))