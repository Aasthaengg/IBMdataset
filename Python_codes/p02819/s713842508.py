num = 0
x = int(input())
while num != 1:
    num = 0
    for i in range(2,x+1):
        if x%i == 0:
            num += 1
    j = x
    x += 1
print(j)