num = int(input())
min = int(input())
diff = -2000000000

for var in range(1,num):
    data = int(input())
    current = data - min
    if current > diff :
        diff = current
    if min > data :
        min = data

print(diff)