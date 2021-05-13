k = int(input())
even = 0
odd = 0
for i in range(k):
    if (i+1)%2 == 0:
        even += 1
    else:
        odd += 1
print(even*odd)