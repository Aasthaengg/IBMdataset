a = int(input())

even, odd = 0, 0

for i in range(a+1):
    if(i == 0):
        continue
    if(i % 2 == 0):
        even += 1
    else:
        odd += 1

print(even * odd)
