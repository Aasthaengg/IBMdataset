N = int(input())

sum = 0
for i in range(N):
    x, y = input().split()
    if(y == "JPY"):
        sum += float(x)
    else:
        sum += float(x)*380000.0
print(sum)
