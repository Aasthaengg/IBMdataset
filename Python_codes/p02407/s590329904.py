n = int(input())
L = list(map(str, input().split()))

LA = L[::-1]
LA = LA[:-1]
LB = L[0]
for i in LA:
 print(i + " ", end="")
print(LB)