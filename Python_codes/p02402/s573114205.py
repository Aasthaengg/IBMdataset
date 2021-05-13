n = int(input())
a = list(map(lambda x: int(x), input().split()))

max = a[0]
min = a[0]
sum = 0

i = 0
while i < n:
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
    sum += a[i]
    i += 1
    
print (str(min) + " " + str(max) + " " + str(sum))

