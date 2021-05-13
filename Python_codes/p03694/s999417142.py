num = int(input())
list = [int(x) for x in input().split()]

list.sort()

print(list[num-1]-list[0])