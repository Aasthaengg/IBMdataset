n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
s = 1
for i in range(n):
    if a[i]%2 == 1:
        s = 0
        break
print(["first","second"][s])