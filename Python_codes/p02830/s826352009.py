n = int(input())
a,b = input().split()
c = []
for i in range(n):
    c.append(''.join(a[i]+b[i]))
print("".join(c))