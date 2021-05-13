x = int(input())

count = 0

count += (x//11)*2
x = x%11

if(1 <= x <= 6):
    count += 1
if(x >= 7):
    count += 2

print(count)