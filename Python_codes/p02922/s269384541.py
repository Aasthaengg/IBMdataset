a,b = input().split(" ")
count = 0
sum = 1
while sum < int(b):
    sum = sum + int(a) -1
    count += 1
print(count)