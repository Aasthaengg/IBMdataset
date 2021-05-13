import sys

a = ""
count = 0
for input in sys.stdin:
    a += (input)
a = a.split()
for i in range(0,len(a)):
    a[i] = int(a[i])
for i in range(a[0],a[1]+1):
    if(a[2] % i == 0):
        count += 1
print count
