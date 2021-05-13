##Addition and Multiplication
prod = 1
n = int(input())
k = int(input())
for x in range(n):
    if (prod < k):
        prod *= 2
    else:
        prod += k
print(prod)