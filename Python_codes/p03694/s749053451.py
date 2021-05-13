n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
print(lst[-1] - lst[0])
