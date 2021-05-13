# ABC056_C
X = int(input())

sum = 0
for i in range(1,X+1):
    sum = sum + i
    if sum >= X:
        break

print(i)