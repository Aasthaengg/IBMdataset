n = int(input())
array = input().split()
reversed_array = []
for i in range(n):
    x = array.pop()
    reversed_array.append(x)
print(" ".join(reversed_array))