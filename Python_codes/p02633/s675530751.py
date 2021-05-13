x = int(input())

for k in range(1, 361):
    n = k*x/360
    if n%1 ==0:
        break
print(k)
