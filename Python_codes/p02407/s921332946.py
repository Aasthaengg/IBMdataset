input()
a = [int(i) for i in input().split()]
print(*a[::-1],sep=" ")
