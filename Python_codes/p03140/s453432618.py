n = int(input())
a = input()
b = input()
c = input()

x = 0
for i,j,k in zip(a,b,c):
    if i != j and j != k and k != i:
        x += 2
    elif i == j and j == k:
        continue
    elif i == j or j == k or k == i:
        x += 1
print(x)

