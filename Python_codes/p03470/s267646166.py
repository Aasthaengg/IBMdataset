n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
x = 0


for i in range(n-1):
    if a[i] == a[i+1]:
        x +=1
print(n-x)
