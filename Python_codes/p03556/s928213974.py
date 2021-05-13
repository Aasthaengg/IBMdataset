n = int(input())
s = 0
for i in range(10**5):
    if i**2 > n:
        break
print((i-1)**2)