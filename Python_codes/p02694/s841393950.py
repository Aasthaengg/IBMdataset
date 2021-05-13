X = int(input())
quota = 100
count = 0
while X > quota:
    quota = quota*101//100
    count += 1
print(count)