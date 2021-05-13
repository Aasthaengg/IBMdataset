n = int(input())
a = list([input() for i in range(n)])
z = 0
ax = 0
for i in range(n):
    a[i] = int(a[i])
    if a[i] > ax:
        z = i
        ax = a[i]
        
print(int(sum(a)-a[z]/2))