N = int(input())
num = N
count = 0
result = 0

while num >= 1:
    num = num / 10
    count += 1

if count % 2 == 0:
    count -= 1
    while count > 0:
        result += 10**(count)-10**(count-1)
        count -= 2
else:
    result = result + N - 10**(count-1) + 1
    count -= 2
    while count > 0:
        result += 10**(count)-10**(count-1)
        count -= 2

print(result)