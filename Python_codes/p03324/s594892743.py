d, n = map(int, input().split())

# print(100 ** 0)
# print(100 ** 1)
# print(100 ** 2)

start = 100 ** d
# step = 100 ** d
# end 

# print(start * n)

value = start
count = 1
while True:
    # print(f'{count} : {value}')
    if n == count:
        break
    
    value += start
    if d == 0:
        if value % 100 != 0:
            count += 1
    elif d == 1:
        if value % 10000 != 0:
            count += 1
    elif d == 2:
        if value % 1000000 != 0:
            count += 1
    else:
        count += 1
    
print(value)