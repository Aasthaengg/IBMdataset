n = int(input())
list_a = [int(x) for x in input().split()]
b = 0

for i in range(n):
    b += 1/list_a[i]

print(1/b)