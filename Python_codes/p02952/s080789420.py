N = int(input())

count = 0
num = 1
while N//num > 0:
    if num*10 <= N:
        count += num*9
    else:
        count += N%(num*10) - num + 1
    num *= 100

print(count)